from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URI, USERS_PER_PAGE
from flask import Blueprint, render_template, url_for, redirect
from project.forms.add_contacts_forms import AddContactForm, SearchContactForm
from project.models import Contact
from project import app, db


@app.route('/add_contact/', methods=['GET', 'POST'])
def add_contact():
    form = AddContactForm()

    if form.validate_on_submit():
        contact = Contact(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            number=str(form.number.data),
            notice=form.notice.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('find_contacts'))
    return render_template('add_contact.html', form=form)


@app.route('/delete_contact/<id>/')
def delete_contact(id):
    contact = Contact.query.filter_by(id=id).first()
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('find_contacts'))


@app.route('/find_contacts/')
@app.route('/find_contacts/<int:page>')
def find_contacts(page=1):
    contacts = Contact.query.order_by(Contact.id.desc()).paginate(page=page, per_page=USERS_PER_PAGE, error_out=False)
    form = SearchContactForm()
    if form.validate_on_submit():
        pass

    return render_template('find_contact.html', contacts=contacts, form=form)


@app.route('/')
def index():
    return render_template('index.html')


