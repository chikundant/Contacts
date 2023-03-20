from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
import os

from config import DB_URI


db = SQLAlchemy()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = os.urandom(12)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI

db.init_app(app)


from project.routes import *
