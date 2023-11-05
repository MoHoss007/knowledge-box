from flask import Blueprint, render_template
from flask import render_template, redirect, url_for, flash, request
from knowledge_box.add_passage.forms import UploadForm, TextForm
from PyPDF2 import PdfReader
import cv2
import io
import numpy as np
from knowledge_box.add_passage.model import OCR
from flask_login import current_user
from knowledge_box.models import User, Passage, db

add_passage = Blueprint("add_passage", __name__, static_folder="static", template_folder="templates")

@add_passage.route("/text", methods=["GET", "POST"])
def text_page():
    form = TextForm()
    text = request.args.get('text')
    name = request.args.get('name')

    if form.validate_on_submit():
        if current_user.is_authenticated:
            user_backref = User.query.filter_by(username=current_user.username).first()
            passage = Passage(
                topic=form.passage_topic.data,
                title=form.passage_name.data,
                text=form.passage_text.data,
                user=user_backref
            )

            db.session.add(passage)
            db.session.commit()

            flash(f"Passage created successfully: {passage.title}", category="success")
            return redirect(url_for("home.home_page"))

    if form.errors != {}:  # form.errors is a dictionary
        for error_message in form.errors.values():
            flash(f"There was an error with uploading: {error_message}", category="danger")

    if text is not None and name is not None:
        form.passage_text.data = text
        form.passage_name.data = name

    return render_template("text.html", form=form)


@add_passage.route("/upload", methods=["GET", "POST"])
def upload_page():
    form = UploadForm()

    if form.validate_on_submit():
        uploaded_file = form.file_upload.data
        upload_type = form.upload_type.data

        text = ""
        name = form.passage_name.data

        if upload_type == 'PDF':
            pdf_file_stream = io.BytesIO(uploaded_file.read())
            pdf_reader = PdfReader(pdf_file_stream)

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        elif upload_type == 'Image':
            ocr = OCR()
            image_stream = io.BytesIO(uploaded_file.read())
            image_stream.seek(0)
            file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            text = ocr.image_to_text(img)

        return redirect(url_for('add_passage.text_page', name=name, text=text))
        # return render_template("text.html", name=name, form=form_text)

    if form.errors != {}:  # form.errors is a dictionary
        for error_message in form.errors.values():
            flash(f"There was an error with uploading: {error_message}", category="danger")

    return render_template("upload.html", form=form)
