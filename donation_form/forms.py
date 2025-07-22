from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange

class DonationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    amount = IntegerField("Amount (₹)", validators=[DataRequired(), NumberRange(min=10)])
    cause = SelectField("Cause", choices=[
        ('education', 'Education'),
        ('healthcare', 'Healthcare'),
        ('environment', 'Environment'),
        ('animal_welfare', 'Animal Welfare')
    ], validators=[DataRequired()])
