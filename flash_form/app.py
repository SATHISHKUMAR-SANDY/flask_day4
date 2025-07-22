from flask import Flask, render_template, redirect, url_for, flash, request
from forms import InfoForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'your_secret_key'
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def form():
    form = InfoForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        age = form.age.data
        accept = form.accept.data

        if "@test.com" in email:
            flash("Emails from test.com are not allowed.", "error")
        elif not accept:
            flash("You must accept the terms and conditions.", "warning")
        else:
            flash(f"Welcome {name}, your form has been submitted successfully!", "success")
            if age > 60:
                flash("You are over 60! Make sure to check senior benefits!", "info")
            return redirect(url_for('success'))
    else:
        if request.method == 'POST':
            flash("Please correct the errors and resubmit the form.", "error")

    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
