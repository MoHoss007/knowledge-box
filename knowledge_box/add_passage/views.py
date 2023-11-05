from flask import Blueprint, render_template

add_passage = Blueprint("add_passage", __name__, static_folder="static", template_folder="templates")


@add_passage.route("/text")
def text_page():
    return render_template("text.html")


@add_passage.route("/upload")
def upload_page():
    return render_template("upload.html")