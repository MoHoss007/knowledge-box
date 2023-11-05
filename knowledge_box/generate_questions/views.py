from flask import Blueprint, render_template

generate_questions = Blueprint("generate_questions", __name__, static_folder="static", template_folder="templates")


@generate_questions.route("choose_passages")
def choose_passages_page():
    return render_template("choose_passages.html")


@generate_questions.route("quiz")
def quiz_page():
    return render_template("quiz.html")
