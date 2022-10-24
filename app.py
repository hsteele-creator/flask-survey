from flask import Flask, render_template
app = Flask(__name__)

# storing customer responses
responses = []

@app.route("/")
def survey():
    return render_template("survey.html")