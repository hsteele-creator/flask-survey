from flask import Flask, render_template, redirect, request
from surveys import satisfaction_survey
app = Flask(__name__)
currentQuestion = -1

# storing customer responses
responses = []

@app.route("/")
def survey():
    return render_template("survey.html", survey=satisfaction_survey, question=currentQuestion)

@app.route("/question/<question>")
def next_question(question):
    question = currentQuestion
    return render_template("question.html", survey=satisfaction_survey, question=currentQuestion)
    