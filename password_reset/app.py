from flask import Flask, render_template, redirect, url_for, flash
from forms import PasswordResetForm

app = Flask(__name__)
app.secret_key = "reset_form_secret"

@app.route("/", methods=["GET", "POST"])
def reset():
    form = PasswordResetForm()
    if form.validate_on_submit():
        flash("Password reset successfully!", "success")
        return redirect(url_for("success"))
    return render_template("reset.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
