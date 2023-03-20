from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, TextAreaField
from wtforms.validators import InputRequired


class AddContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    surname = StringField('Surname')
    email = EmailField('Email')
    number = StringField('Phone number', validators=[InputRequired()])
    notice = TextAreaField('Notice')
    submit = SubmitField('Save')
