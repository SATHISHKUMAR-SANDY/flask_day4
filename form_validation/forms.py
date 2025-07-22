from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Regexp, Optional, ValidationError

def block_test_domain(form, field):
    if field.data.endswith('@test.com'):
        raise ValidationError('Emails from test.com are not allowed.')

class CustomForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(message="Name is required."),
        Length(min=3, max=30, message="Name must be between 3 and 30 characters."),
        Regexp(r'^[a-zA-Z]+$', message="Name must contain only letters.")
    ])

    username = StringField("Username", validators=[
        DataRequired(message="Username required."),
        Length(min=6, message="Username must be more than 5 characters.")
    ])

    email = StringField("Email", validators=[
        DataRequired(message="Email is required."),
        Email(message="Invalid email format."),
        block_test_domain
    ])

    password = PasswordField("Password", validators=[
        DataRequired(message="Password is required."),
        Length(min=6, message="Password must be at least 6 characters.")
    ])

    confirm = PasswordField("Confirm Password", validators=[
        DataRequired(message="Confirm your password."),
        EqualTo('password', message="Passwords must match.")
    ])

    age = IntegerField("Age", validators=[
        DataRequired(message="Age is required."),
        NumberRange(min=18, max=60, message="Age must be between 18 and 60.")
    ])

    nickname = StringField("Nickname (Optional)", validators=[Optional()])

    accept = BooleanField("I accept the terms", validators=[
        DataRequired(message="You must accept the terms.")
    ])

    submit = SubmitField("Register")
