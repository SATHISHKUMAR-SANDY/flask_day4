from flask import Flask, render_template, redirect, url_for, flash
from forms import DonationForm

app = Flask(__name__)
app.secret_key = "donation_secret"

@app.route("/", methods=["GET", "POST"])
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        amount = form.amount.data
        cause = form.cause.data
        flash(f"Thank you! You donated ₹{amount} for {cause}.", "success")
        return redirect(url_for("thank_you"))
    return render_template("donate.html", form=form)

@app.route("/thank-you")
def thank_you():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
