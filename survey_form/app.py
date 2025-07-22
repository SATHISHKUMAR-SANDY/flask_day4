from flask import Flask, render_template, redirect, url_for, flash
from forms import SurveyForm

app = Flask(__name__)
app.secret_key = "survey_form_secret"

@app.route("/", methods=["GET", "POST"])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        flash("Thanks for participating!", "success")
        return redirect(url_for("success"))
    return render_template("survey.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
