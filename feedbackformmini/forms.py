from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional, Email

class FeedbackForm(FlaskForm):
    name = StringField("Name")
    email = StringField("Email", validators=[Optional(), Email()])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10)])
