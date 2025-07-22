from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class SurveyForm(FlaskForm):
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=18, max=100)])
    gender = SelectField("Gender", choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")], validators=[DataRequired()])
    favorite_product = SelectField("Favorite Product", choices=[("Laptop", "Laptop"), ("Mobile", "Mobile"), ("Tablet", "Tablet")], validators=[DataRequired()])
    feedback = TextAreaField("Feedback", validators=[DataRequired()])
