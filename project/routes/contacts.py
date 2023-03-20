from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URI
from flask import Blueprint, render_template, url_for, redirect
from project.forms.add_contacts_forms import AddContactForm
from project.models import Contact


contacts = Blueprint('contacts', __name__)

engine = create_engine(DB_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@contacts.route('/add_contact/', methods=['GET', 'POST'])
def add_contact():
    form = AddContactForm()

    if form.validate_on_submit():
        contact = Contact(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            number=form.number.data,
            notice=form.notice.data
        )
        session.add(contact)
        session.commit()
    return render_template('add_contact.html', form=form)


@contacts.route('/explore_contacts/')
def explore_contacts():
    pass

