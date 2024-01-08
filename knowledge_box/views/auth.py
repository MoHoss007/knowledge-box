from flask import Blueprint, render_template
from flask import render_template, redirect, url_for, flash
from knowledge_box.repositories.user_repository import UserRepository
from knowledge_box.forms.auth import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required

auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = UserRepository.create_user(username=form.username.data,
                                                    email=form.email.data,
                                                    password=form.password.data)

        login_user(user_to_create)
        flash(f"Account created successfully: {user_to_create.username}", category="success")
        return redirect(url_for("home.home_page"))

    if form.errors != {}:  # form.errors is a dictionary
        for error_message in form.errors.values():
            flash(f"There was an error with creating a user: {error_message}", category="danger")

    return render_template("auth/register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():

        corresponding_user = UserRepository.get_user_by_name_or_email(form.username_or_email.data)

        if corresponding_user and corresponding_user.check_password(form.password.data):
            login_user(corresponding_user)
            flash(f"Successfully logged in as: {corresponding_user.username}", category="success")
            return redirect(url_for("home.home_page"))
        else:
            flash("Incorrect email or password.", category="danger")

    return render_template("auth/login.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", category="info")
    return redirect(url_for("home.home_page"))
