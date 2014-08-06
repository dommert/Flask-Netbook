# Flask-Netbook Version 0.0.1
# Models.py

import datetime
# Flask
from flask import Flask
# PeeWee
from peewee import *
# Turbo-Duck
from flask_turboduck import *
from flask_turboduck.auth import Auth, BaseUser
# Netbook
from app import app, db, auth
from config import Configuration


# -----------------------------------------------------
# Note Class
class Note(db.Model):
    created = DateTimeField(default=datetime.datetime.now)
    message = BlobField()

# User Class
