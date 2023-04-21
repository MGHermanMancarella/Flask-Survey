from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.get("/")
def start_survey():
    """start the survey"""
    return render_template("survey_start.html",
    survey=survey)

@app.post("/begin")
def question_redirect():
    """redirect to first question"""

    session["responses"] = []
    responses.clear()
    return redirect("/question/0")

@app.get("/question/<int:q_num>")
def populate_question(q_num):
    """populate current iteration of question/answers"""

    answers = survey.questions[q_num].choices
    question = survey.questions[q_num]
    return render_template("question.html", question=question, choices=answers)

@app.post("/answer")
def answer_redirect():
    """redirects and saves responses"""

    responses.append(request.form['answer'])

    if  len(responses) == len(survey.questions):
        return render_template('completion.html', responses=responses, questions=survey.questions)
    else:
        return redirect(f"/question/{len(responses) }")