from flask import Flask, render_template, redirect, flash, url_for
from forms import NewsletterForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'your_secret_key'
csrf = CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
def subscribe():
    form = NewsletterForm()
    if form.validate_on_submit():
        flash("Subscribed successfully!", "success")
        return render_template("success.html", name=form.name.data)
    return render_template("subscribe.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
