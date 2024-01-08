from flask import render_template, redirect, url_for, flash, request, Blueprint, current_app
from knowledge_box.forms.add_passage import UploadForm, TextForm
import cv2
import io
import numpy as np
from flask_login import current_user
from knowledge_box.repositories.passage_repository import PassageRepository
from knowledge_box.repositories.user_repository import UserRepository

add_passage = Blueprint("add_passage", __name__, static_folder="static", template_folder="templates")


@add_passage.route("/text", methods=["GET", "POST"])
def text_page():
    form = TextForm()
    text = request.args.get('text')
    name = request.args.get('name')

    if form.validate_on_submit():
        if current_user.is_authenticated:
            user_backref = UserRepository.get_user_by_name_or_email(current_user.username)
            passage = PassageRepository.create_passage(
                topic=form.passage_topic.data,
                title=form.passage_name.data,
                text=form.passage_text.data,
                user=user_backref
            )

            flash(f"Passage created successfully: {passage.title}", category="success")
            return redirect(url_for("home.home_page"))

    if form.errors != {}:  # form.errors is a dictionary
        for error_message in form.errors.values():
            flash(f"There was an error with uploading: {error_message}", category="danger")

    if text is not None and name is not None:
        form.passage_text.data = text
        form.passage_name.data = name

    return render_template("add_passage/text.html", form=form)


@add_passage.route("/upload", methods=["GET", "POST"])
def upload_page():
    form = UploadForm()

    if form.validate_on_submit():
        uploaded_file = form.file_upload.data
        upload_type = form.upload_type.data

        text = ""
        name = form.passage_name.data
        uploaded_file = io.BytesIO(uploaded_file.read())

        if upload_type == 'PDF':
            text = current_app.ocr_service.pdf_to_text(uploaded_file)

        elif upload_type == 'Image':
            text = current_app.ocr_service.img_to_text(uploaded_file)

        return redirect(url_for('add_passage.text_page', name=name, text=text))

    if form.errors != {}:  # form.errors is a dictionary
        for error_message in form.errors.values():
            flash(f"There was an error with uploading: {error_message}", category="danger")

    return render_template("add_passage/upload.html", form=form)
