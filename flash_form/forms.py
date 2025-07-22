from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Regexp, Optional

class InfoForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(message="Name is required."),
        Length(min=3, message="Name must be at least 3 characters."),
        Regexp("^[A-Za-z]+$", message="Name must contain only letters.")
    ])
    email = StringField("Email", validators=[
        DataRequired(message="Email is required."),
        Email(message="Invalid email format.")
    ])
    age = IntegerField("Age", validators=[
        DataRequired(message="Age is required."),
        NumberRange(min=18, max=100, message="Age must be between 18 and 100.")
    ])
    accept = BooleanField("Accept Terms", validators=[
        DataRequired(message="You must accept the terms.")
    ])
    submit = SubmitField("Submit")
