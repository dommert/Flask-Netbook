# Flask-Netbook Version 0.0.1
# Admin.py

from app import app, db
from auth import auth
from models import User, Note
from flask import request
from flask_turboduck.admin import Admin, ModelAdmin, AdminPanel

admin = Admin(app, auth, branding='Example Site')
auth.register_admin(admin)
admin.register(Note)
admin.register(User)