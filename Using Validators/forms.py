from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, BooleanField, DateField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class MessageForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(message="Name is required."),
        Length(min=2, max=30, message="Name must be between 2 and 30 characters.")
    ])

    email = StringField("Email", validators=[
        DataRequired(message="Email is required."),
        Email(message="Enter a valid email address.")
    ])

    message = TextAreaField("Message", validators=[
        DataRequired(message="Message is required.")
    ])

    gender = RadioField("Gender", choices=[
        ('male', 'Male'), ('female', 'Female')
    ], validators=[DataRequired(message="Please select your gender.")])

    accept_term = BooleanField("I accept the terms", validators=[
        DataRequired(message="You must accept the terms.")
    ])

    date = DateField("Date", validators=[
        DataRequired(message="Date is required.")
    ])

    age = IntegerField("Age", validators=[
        DataRequired(message="Age is required."),
        NumberRange(min=1, max=120, message="Age must be between 1 and 120.")
    ])

    submit = SubmitField("Submit")
