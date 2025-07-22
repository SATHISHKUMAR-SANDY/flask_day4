from flask import Flask, render_template, redirect, url_for, flash
from forms import BugReportForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route("/", methods=["GET", "POST"])
def report():
    form = BugReportForm()
    if form.validate_on_submit():
        severity = form.severity.data
        if severity == "Low":
            flash("Bug reported successfully. Severity: LOW. Thank you!", "success")
        elif severity == "Medium":
            flash("Bug reported successfully. Severity: MEDIUM. We’ll look into it soon.", "warning")
        else:
            flash("Critical Bug! Severity: HIGH. Our team has been alerted!", "danger")
        return redirect(url_for("thank_you"))
    return render_template("report.html", form=form)

@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)
