from flask import Flask, render_template, redirect, url_for, flash
from forms import TicketForm
import random
import string

app = Flask(__name__)
app.secret_key = "support_secret"

def generate_ticket_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@app.route("/", methods=["GET", "POST"])
def ticket():
    form = TicketForm()
    if form.validate_on_submit():
        ticket_id = generate_ticket_id()
        flash(f"Support ticket created. Ticket ID: {ticket_id}", "success")
        return redirect(url_for("success"))
    return render_template("ticket.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
