from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from project import db


class Contact(UserMixin, db.Model):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    surname = Column(String(50))
    email = Column(String(50))
    number = Column(String(50), unique=True)
    notice = Column(String(200))

    def __repr__(self):
        return '<Contact {}>'.format(self.id)
