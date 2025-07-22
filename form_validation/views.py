from flask import Blueprint, render_template, redirect, url_for, flash
from forms import CustomForm

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def register():
    form = CustomForm()
    if form.validate_on_submit():
        flash("Registration Successful!", "success")
        return redirect(url_for("views.register"))

    error_count = len(form.errors)
    return render_template("form.html", form=form, error_count=error_count)
