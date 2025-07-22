from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class CourseEnrollmentForm(FlaskForm):
    name = StringField("Student Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    course = SelectField("Course", choices=[("Python", "Python"), ("Web Dev", "Web Development"), ("Data Science", "Data Science")], validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=18, max=60)])
    submit = SubmitField("Enroll")
