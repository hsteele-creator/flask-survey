from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey
app = Flask(__name__)
app.config['SECRET_KEY'] = 'potato'
DebugToolbarExtension(app)
DEBUG_TB_INTERCEPT_REDIRECTS = False

# storing customer responses
responses = []

@app.route("/")
def survey():
    return render_template("survey.html", survey=satisfaction_survey)

@app.route("/question/<int:question>")
def next_question(question):
    
    if question < 4:      
        return render_template("question.html", survey=satisfaction_survey, page=question)
    else:
        return render_template("thank-you.html")


@app.route("/answers", methods=["POST"])
def answer():
    answer = request.form["answer"]
    responses.append(answer)
    
    return redirect(f"/question/{len(responses)}")
    
    