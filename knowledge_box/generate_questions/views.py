from flask import Blueprint, render_template, redirect, request, url_for
from knowledge_box.models import Passage
from knowledge_box.generate_questions.forms import ProceedForm
from knowledge_box.models import Passage
from knowledge_box.generate_questions.model import GenerateQuestions

generate_questions = Blueprint("generate_questions", __name__, static_folder="static", template_folder="templates")

generator = GenerateQuestions()


@generate_questions.route("/choose_passages", methods=["GET", "POST"])
def choose_passages_page():
    proceed_form = ProceedForm()

    if proceed_form.validate_on_submit():
        selected_passage_titles = [value for value in request.form.getlist("passages")]

        delimiter = "$DELIMITER$"
        selected_passage_titles_str = delimiter.join(selected_passage_titles)
        return redirect(url_for("generate_questions.quiz_page", selected_passage_titles_str=selected_passage_titles_str))

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
    delimiter = "$DELIMITER$"
    selected_passage_titles_str = request.args.get("selected_passage_titles_str")
    selected_passage_titles = selected_passage_titles_str.split(delimiter)

    passages = [Passage.query.filter_by(title=title).first() for title in selected_passage_titles]

    quiz = list()
    for passage in passages:
        temp_quiz = generator.generate(passage.text)
        quiz += temp_quiz

    for mcq in quiz:
        print(mcq["question_text"])

    return render_template("quiz.html", quiz=quiz)
