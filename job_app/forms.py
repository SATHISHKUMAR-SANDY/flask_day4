from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, URL, NumberRange

class JobApplicationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    resume = StringField("Resume URL", validators=[DataRequired(), URL()])
    experience = IntegerField("Experience (years)", validators=[DataRequired(), NumberRange(min=0)])
