from flask import Flask, render_template, redirect, url_for, flash
from forms import FeedbackForm

app = Flask(__name__)
app.secret_key = "student_feedback_secret"

@app.route("/", methods=["GET", "POST"])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        rating = form.rating.data
        if rating < 5:
            flash("We'll improve!", "warning")
        else:
            flash("Thanks for your feedback!", "success")
        return redirect(url_for("success"))
    return render_template("feedback.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
