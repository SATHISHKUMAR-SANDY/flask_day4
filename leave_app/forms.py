from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import DataRequired

class LeaveForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])
    reason = TextAreaField("Reason", validators=[DataRequired()])
    start_date = DateField("Start Date", validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField("End Date", validators=[DataRequired()], format='%Y-%m-%d')
