from flask import Flask, render_template, redirect, url_for, flash
from forms import JobApplicationForm

app = Flask(__name__)
app.secret_key = "job123"

@app.route("/", methods=["GET", "POST"])
def apply():
    form = JobApplicationForm()
    if form.validate_on_submit():
        flash("Application submitted successfully!", "success")
        return redirect(url_for("success"))
    return render_template("apply.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
