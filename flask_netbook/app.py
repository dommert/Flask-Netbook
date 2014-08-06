# Flask-Netbook Version 0.0.1
# App.py

# Flask
from flask import Flask
# Flask-TurboDuck
from flask_turboduck.db import Database
from flask_turboduck.auth import Auth
# Netbook


app = Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)
auth = Auth(app, db)
