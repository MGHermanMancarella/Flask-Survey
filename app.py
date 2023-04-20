from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

reponses = []
quest_num = 0

@app.get("/")
def start_survey():
    return render_template("survey_start.html",
    survey_title=survey.title,
    survey_instructions = survey.instructions)
#inject survey

@app.post("/begin")
def question_redirect():
    return redirect("/question/0")

@app.get("/question/<int:q_num>")
def populate_question(q_num):
    global quest_num
    quest_num = q_num + 1
    answers = survey.questions[q_num].choices
    question = survey.questions[q_num]
    return render_template("question.html", question=question, choices=answers)

@app.post("/answer")
def answer_redirect():
    return redirect(f"/question/{quest_num}")