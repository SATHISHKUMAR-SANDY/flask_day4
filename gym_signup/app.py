from flask import Flask, render_template, redirect, url_for, flash
from forms import GymSignupForm

app = Flask(__name__)
app.secret_key = "signup_secret"

@app.route("/", methods=["GET", "POST"])
def signup():
    form = GymSignupForm()
    if form.validate_on_submit():
        flash(f"Welcome to our gym, {form.name.data}!", "success")
        return redirect(url_for("success"))
    return render_template("signup.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
