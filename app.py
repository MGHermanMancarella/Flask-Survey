from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []
quest_num = 0

@app.get("/")
def start_survey():
    """start the survey"""

    return render_template("survey_start.html",
    survey=survey)

@app.post("/begin")
def question_redirect():
    """redirect to first question"""
    responses.clear()
    return redirect("/question/0")

@app.get("/question/<int:q_num>")
def populate_question(q_num):
    """populate current iteration of question/answers"""
    global quest_num
    quest_num = q_num + 1
    answers = survey.questions[q_num].choices
    question = survey.questions[q_num]
    return render_template("question.html", question=question, choices=answers)

@app.post("/answer")
def answer_redirect():
    """redirects and saves responses"""
    global responses, quest_num
    responses.append((survey.questions[quest_num-1].prompt, request.form['answer']))
    if quest_num == len(survey.questions):
        return render_template('completion.html', responses=responses)
    else:
        return redirect(f"/question/{quest_num}")