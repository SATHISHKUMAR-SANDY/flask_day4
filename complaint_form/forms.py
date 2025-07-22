from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length

class ComplaintForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    complaint = TextAreaField("Complaint", validators=[DataRequired(), Length(min=15)])
    category = SelectField("Category", choices=[
        ('billing', 'Billing'),
        ('technical', 'Technical'),
        ('service', 'Customer Service'),
        ('other', 'Other')
    ], validators=[DataRequired()])
