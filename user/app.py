from flask import Flask, render_template, flash, redirect, url_for
from forms.register import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Welcome, {form.full_name.data}!", "success")
        return redirect(url_for("register"))
    else:
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {field}: {error}", "danger")
    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
