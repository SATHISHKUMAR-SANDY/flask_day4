from flask import Flask, render_template, redirect, url_for, flash
from forms import ComplaintForm
import random

app = Flask(__name__)
app.secret_key = "complaint_secret"

@app.route("/", methods=["GET", "POST"])
def complaint():
    form = ComplaintForm()
    if form.validate_on_submit():
        complaint_id = f"CMP-{random.randint(1000,9999)}"
        flash(f"Complaint registered successfully! Your ID is {complaint_id}", "success")
        return redirect(url_for("success"))
    return render_template("complaint.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
