from flask import Blueprint, render_template
from flask import render_template, redirect, url_for, flash
from blog.models import User
from blog.auth.forms import RegisterForm, LoginForm
from blog.models import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )

        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f"Account created successfully: {user_to_create.username}", category="success")
        return redirect(url_for("home.home_page"))

    if form.errors != {}:  # form.errors is a dictionary
        for error_message in form.errors.values():
            flash(f"There was an error with creating a user: {error_message}", category="danger")

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        corresponding_user = User.query.filter(
            (User.username == form.username_or_email.data) | (User.email == form.username_or_email.data)
        ).first()

        if corresponding_user and corresponding_user.check_password(form.password.data):
            login_user(corresponding_user)
            flash(f"Successfully logged in as: {corresponding_user.username}", category="success")
            return redirect(url_for("home.home_page"))
        else:
            flash("Incorrect email or password.", category="danger")

    return render_template("login.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", category="info")
    return redirect(url_for("home.home_page"))
