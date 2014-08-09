# Flask-Netbook Version 0.0.2
# Auth.py

from flask_turboduck.auth import Auth

from app import app, db
from models import User

# Authentication wrapper for TurboDuck
auth = Auth(app, db, user_model=User)