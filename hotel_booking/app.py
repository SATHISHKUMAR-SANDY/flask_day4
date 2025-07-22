from flask import Flask, render_template, redirect, url_for, flash
from forms import BookingForm

app = Flask(__name__)
app.secret_key = "hotel_secret"

@app.route("/", methods=["GET", "POST"])
def book():
    form = BookingForm()
    if form.validate_on_submit():
        name = form.name.data
        room = form.room_type.data
        nights = form.nights.data
        flash(f"Booking for {name} confirmed: {nights} nights in {room}", "success")
        return redirect(url_for("confirm"))
    return render_template("book.html", form=form)

@app.route("/confirm")
def confirm():
    return render_template("confirm.html")

if __name__ == "__main__":
    app.run(debug=True)
