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
#     return redirect("/questions")

# @app.get("/questions")
# def populate_question():
    return render_template("question.html")