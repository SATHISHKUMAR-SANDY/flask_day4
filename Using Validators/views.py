# views.py
from flask import Blueprint, render_template, redirect, url_for
from forms import MessageForm

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def form_page():
    form = MessageForm()
    if form.validate_on_submit():
        # Handle valid form (e.g., save data)
        return redirect(url_for('views.success_page'))
    return render_template('form.html', message=form)

@views.route('/success')
def success_page():
    return "Form submitted successfully!"
