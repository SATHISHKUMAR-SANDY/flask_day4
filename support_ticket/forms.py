from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class TicketForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    issue_category = SelectField("Issue Category", choices=[
        ("billing", "Billing"),
        ("technical", "Technical Issue"),
        ("general", "General Inquiry")
    ], validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired(), Length(min=25)])
