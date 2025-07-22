from flask import Flask, render_template, redirect, flash, url_for
from forms import AppointmentForm

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def book():
    form = AppointmentForm()
    if form.validate_on_submit():
        name = form.name.data
        date = form.date.data
        time = form.time.data
        flash(f"Appointment confirmed for {name} on {date} at {time}", "success")
        return redirect(url_for("success"))
    return render_template("appointment_form.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
