# Flask-Netbook Version 0.0.1
# Models.py

import datetime
from app import db
from peewee import *
from flask_turboduck.auth import BaseUser


# -----------------------------------------------------
# User Class
class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    def __unicode__(self):
        return self.username

# Note Class
class Note(db.Model):
    created = DateTimeField(default=datetime.datetime.now)
    message = BlobField()

