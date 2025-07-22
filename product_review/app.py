from flask import Flask, render_template, redirect, url_for, flash
from forms import ReviewForm

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/", methods=["GET", "POST"])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        flash("Thank you for your review!", "success")
        return redirect(url_for("thankyou"))
    return render_template("review.html", form=form)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
