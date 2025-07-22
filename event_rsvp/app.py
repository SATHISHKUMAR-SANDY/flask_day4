from flask import Flask, render_template, redirect, url_for, flash
from forms import RSVPForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route("/", methods=["GET", "POST"])
def rsvp():
    form = RSVPForm()
    if form.validate_on_submit():
        if not form.will_attend.data:
            flash("Sorry to miss you", "warning")
        else:
            flash("Thank you for your RSVP", "success")
        return redirect(url_for("response"))
    return render_template("rsvp.html", form=form)

@app.route("/response")
def response():
    return render_template("response.html")

if __name__ == "__main__":
    app.run(debug=True)
