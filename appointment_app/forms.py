from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField
from wtforms.validators import DataRequired, Email

class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    date = DateField("Date", validators=[DataRequired()], format='%Y-%m-%d')
    time = TimeField("Time", validators=[DataRequired()], format='%H:%M')
    purpose = TextAreaField("Purpose", validators=[DataRequired()])
