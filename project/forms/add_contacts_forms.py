from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, TextAreaField, SelectField
from wtforms.validators import InputRequired, ValidationError
from project.models import Contact


class AddContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    surname = StringField('Surname')
    email = EmailField('Email')
    number = StringField('Phone number', validators=[InputRequired()])
    notice = TextAreaField('Notice')
    submit = SubmitField('Save')
    def validate_number(self, number):
        contact = Contact.query.filter_by(number=str(number.data)).first()
        if contact is not None:
            raise ValidationError('Number already exists')


class SearchContactForm(FlaskForm):
    inpt = StringField()
    submit = SubmitField('Find')
    search = SelectField('Search by', choices=[
        'name',
        'surname',
        'email',
        'number'])
