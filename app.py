from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey
app = Flask(__name__)
app.config['SECRET_KEY'] = 'potato'
DebugToolbarExtension(app)
DEBUG_TB_INTERCEPT_REDIRECTS = False

question_number = [-1]
current_number = [-1]
currentQuestion = -1



# storing customer responses
responses = []

@app.route("/")
def survey():
    
    current_page = -1
    next_page = current_page + 1
    current_page = next_page  

    return render_template("survey.html", survey=satisfaction_survey, question = next_page)

@app.route("/question/<question>")
def next_question(question):
    
    current_page = -1
    next_page = current_page + 1
    current_page = next_page
    
    return render_template("question.html", survey=satisfaction_survey, question = next_page)


@app.route("/answers", methods=["POST"])
def answer():
    answer = request.form["answer"]
    responses.append(answer)
    
    return redirect(f"/question/5")
    
    