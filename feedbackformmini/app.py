from flask import Flask, render_template, flash, redirect, url_for
from forms import FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('success'))
    return render_template('feedback.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')
