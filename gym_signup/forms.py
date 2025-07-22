from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, NumberRange, InputRequired

class GymSignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=16)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    plan = SelectField("Plan", choices=[
        ("monthly", "Monthly"),
        ("yearly", "Yearly")
    ], validators=[InputRequired()])
    accept_terms = BooleanField("I accept the Terms & Conditions", validators=[DataRequired()])
