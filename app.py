from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

reponses = []

@app.get("/")
def start_survey():
    return render_template("survey_start.html",
    survey_title=survey.title,
    survey_instructions = survey.instructions)

@app.post("/begin")
def question_redirect():
    return redirect('/question')

@app.get("/question/<int:q_num>")
def populate_question():
    ##NOTE: Create q_num variable for the question we're on
    ##QUESTION: Global? If we redeclare in this method will it be available again?
    answers = survey.questions[2].choices
    question = survey.questions[2].prompt
    # @app.get("/questions")
    # def populate_question()
    return render_template("question.html", question_prompt=question, choices=answers)