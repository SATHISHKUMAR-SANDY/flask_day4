# app.py
from flask import Flask
from views import views

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Register blueprint
app.register_blueprint(views)

if __name__ == '__main__':
    app.run(debug=True)
