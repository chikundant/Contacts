from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from config import DB_URI
from project.models import Base, Contact

from project.routes.main import main as main_blueprint
from project.routes.contacts import contacts as contacts_blueprint

engine = create_engine(DB_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = os.urandom(12)
app.config["SQLALCHEMY_DATABASE_URI"] = engine
Base.metadata.create_all(engine)

app.register_blueprint(main_blueprint)
app.register_blueprint(contacts_blueprint)


from project.routes import *