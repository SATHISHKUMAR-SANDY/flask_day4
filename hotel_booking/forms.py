from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange

class BookingForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    room_type = SelectField("Room Type", choices=[
        ("Single", "Single"),
        ("Double", "Double"),
        ("Suite", "Suite")
    ], validators=[DataRequired()])
    nights = IntegerField("Nights", validators=[DataRequired(), NumberRange(min=1)])
