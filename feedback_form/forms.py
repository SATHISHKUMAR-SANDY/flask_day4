from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class FeedbackForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(message="Name is required."),
        Length(min=3, message="Name must be at least 3 characters.")
    ])
    age = IntegerField("Age", validators=[
        DataRequired(message="Age is required."),
        NumberRange(min=18, max=60, message="Age must be between 18 and 60.")
    ])
    submit = SubmitField("Submit")
