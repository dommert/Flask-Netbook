# Flask-Netbook Version 0.0.1
# App.py

# Flask
from flask import Flask
# Netbook
    #from models import *
    #from views import *

app = Flask(__name__)
app.config.from_object('config.Configuration')

# db = Database(app)


