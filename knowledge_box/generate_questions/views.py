from flask import Blueprint, render_template, redirect, request, url_for
from knowledge_box.models import Passage
from knowledge_box.generate_questions.forms import ProceedForm

generate_questions = Blueprint("generate_questions", __name__, static_folder="static", template_folder="templates")


@generate_questions.route("/choose_passages", methods=["GET", "POST"])
def choose_passages_page():
    proceed_form = ProceedForm()

    if proceed_form.validate_on_submit():
        selected_passage_titles = [value for value in request.form.getlist("passages")]

        quiz_resources = {}
        for selected_passage_title in selected_passage_titles:
            quiz_resources[selected_passage_title] = Passage.query.filter_by(
                title=selected_passage_title
            ).first().text

        return render_template("quiz.html", quiz_resources=quiz_resources)

    topics = [
        "mathematics",
        "physics",
        "chemistry",
        "biology",
        "psychology",
        "history"
    ]

    passages = Passage.query.all()

    return render_template("choose_passages.html", proceed_form=proceed_form, topics=topics, passages=passages)


@generate_questions.route("/quiz")
def quiz_page():
    return render_template("quiz.html")
