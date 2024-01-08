from flask import Blueprint, render_template, redirect, request, url_for, current_app
from knowledge_box.utils.question_generator import GenerateQuestions
from knowledge_box.forms.generate_questions import ProceedForm
from knowledge_box.repositories.passage_repository import PassageRepository

generate_questions = Blueprint("generate_questions", __name__, static_folder="static", template_folder="templates")


@generate_questions.route("/choose_passages", methods=["GET", "POST"])
def choose_passages_page():
    proceed_form = ProceedForm()

    if proceed_form.validate_on_submit():
        selected_passage_titles = [value for value in request.form.getlist("passages")]

        delimiter = "$DELIMITER$"
        selected_passage_titles_str = delimiter.join(selected_passage_titles)
        return redirect(url_for("generate_questions.quiz_page", selected_passage_titles_str=selected_passage_titles_str))

    passages = PassageRepository.get_all_passages()

    return render_template("generate_questions/choose_passages.html", proceed_form=proceed_form, topics=current_app.topics, passages=passages)


@generate_questions.route("/quiz")
def quiz_page():
    delimiter = "$DELIMITER$"
    selected_passage_titles_str = request.args.get("selected_passage_titles_str")
    selected_passage_titles = selected_passage_titles_str.split(delimiter)

    passages = [PassageRepository.get_passage_by_title(title) for title in selected_passage_titles]

    quiz = list()
    for passage in passages:
        temp_quiz = GenerateQuestions.generate(passage.text)
        quiz += temp_quiz

    for mcq in quiz:
        print(mcq["question_text"])

    return render_template("generate_questions/quiz.html", quiz=quiz)
