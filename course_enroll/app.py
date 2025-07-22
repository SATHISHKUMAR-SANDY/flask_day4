from flask import Flask, render_template, redirect, flash, url_for
from forms import CourseEnrollmentForm  # ✅ Correct class name

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/", methods=["GET", "POST"])
def enroll():
    form = CourseEnrollmentForm()
    if form.validate_on_submit():
        name = form.name.data
        course = form.course.data
        flash(f"Hi {name}, you enrolled in {course}", "success")
        return redirect(url_for("success"))
    return render_template("enroll.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
