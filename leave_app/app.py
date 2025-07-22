from flask import Flask, render_template, redirect, url_for, flash
from forms import LeaveForm
from datetime import datetime

app = Flask(__name__)
app.secret_key = "leave123"

@app.route("/", methods=["GET", "POST"])
def leave():
    form = LeaveForm()
    if form.validate_on_submit():
        start = form.start_date.data
        end = form.end_date.data
        duration = (end - start).days + 1

        if end < start:
            form.end_date.errors.append("End date cannot be before start date.")
            return render_template("leave_form.html", form=form)

        flash(f"You applied for {duration} day(s) of leave", "success")
        return redirect(url_for("success"))
    return render_template("leave_form.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
