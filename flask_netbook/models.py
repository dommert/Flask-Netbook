# Flask-Netbook Version 0.0.1
# Models.py

import datetime
# Flask
from flask import Flask
# PeeWee
from peewee import *
# Turbo-Duck
from flask_turboduck.auth import Auth, BaseUser
# Netbook
from app import app, db, auth


# -----------------------------------------------------
# User Class
class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()

# Note Class
class Note(db.Model):
    created = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User)
    message = BlobField()

auth.User.create_table(fail_silently=True)
Note.create_table(fail_silently=True)