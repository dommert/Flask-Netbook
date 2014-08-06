# Flask-Netbook Version 0.0.1
# App.py

from flask import Flask
from app import app, db
from views import *
from models import *


app = Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)


