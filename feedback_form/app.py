from flask import Flask, render_template, request, redirect, flash
from forms import FeedbackForm

app = Flask(__name__)
app.secret_key = 'secret-key'

@app.route('/', methods=['GET', 'POST'])
def form_page():
    form = FeedbackForm()
    if form.validate_on_submit():
        flash("Form submitted successfully!", "success")
        return redirect('/')
    elif request.method == 'POST':
        flash("Form has errors!", "error")
        print("❌ Form Errors:", form.errors)  # Logging errors to terminal

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
