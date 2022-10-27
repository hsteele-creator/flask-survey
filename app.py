from curses import curs_set
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey
app = Flask(__name__)
app.config['SECRET_KEY'] = 'potato'
DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# storing customer responses
responses = []

@app.route("/")
def survey():
    return render_template("survey.html", survey=satisfaction_survey)

@app.route("/question/<int:question>")
def next_question(question):
    
    cur_session = session["responses"]
    
    if(len(cur_session) != question):
        flash("Sorry, you must answer all of the questions in order")
        return redirect(f"/question/{len(cur_session)}")
    
    if question < 4:      
        return render_template("question.html", survey=satisfaction_survey, page=question)
    else:
        return render_template("thank-you.html")


@app.route("/answers", methods=["POST"])
def answer():
    answer = request.form["answer"]
    # responses.append(answer)
    cur_session = session["responses"]
    cur_session.append(answer)
    session["responses"] = cur_session
    
    return redirect(f"/question/{len(cur_session)}")

@app.route("/start_survey", methods=["POST"])
def start_session():
    session["responses"] = []
    return redirect("/question/0")
    