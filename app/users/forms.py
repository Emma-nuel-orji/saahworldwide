from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField('Please input your full Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State/ Province', validators=[DataRequired()])
    code = StringField('Postal/ Zip Code', validators=[DataRequired()])
    address = TextAreaField('Current Address', validators=[DataRequired()])
    date = DateField('Date Of Birth', validators=[DataRequired()])
    employ = StringField('Employed, Self-Employed or Un-Employed', validators=[DataRequired()])
    education = StringField('Your Education Level', validators=[DataRequired()])
    position = StringField('What position are you applying for?', validators=[DataRequired()])
    yes = StringField('Are you in UAE or outside UAE?', validators=[DataRequired()])
    media = StringField('Where did you hear about us?', validators=[DataRequired()])
    remember = BooleanField('By clicking on the above check box, you agree the our terms and condition ')
    submit = SubmitField('submit')

