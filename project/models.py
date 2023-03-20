from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Contact(UserMixin, Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    surname = Column(String(50))
    email = Column(String(50))
    number = Column(String(50), unique=True)
    notice = Column(String(200))
