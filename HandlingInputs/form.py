from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Email
from wtforms import TextAreaField,RadioField,BooleanField,DateField,IntegerField



class messageForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email()])
    message = TextAreaField("Your Message",validators=[DataRequired()])
    submit = SubmitField("Submit")
    gender = RadioField("Choose one",choices=[('A','male'),('B','female')],validators=[DataRequired()])
    accept_term = BooleanField("Accept the terms",validators=[DataRequired()])
    date = DateField("Event Date", format='%Y-%m-%d', validators=[DataRequired()])
    age = IntegerField("Your age",validators=[DataRequired()])
    




