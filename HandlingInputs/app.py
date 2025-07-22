from flask import Flask, render_template, request, flash, redirect, url_for 

from form import messageForm
from view import views

app = Flask(__name__)

app.config['SECRET_KEY']='your_secret_key_here'

app.register_blueprint(views)

if __name__ == '__main__':
    app.run(debug=True)
