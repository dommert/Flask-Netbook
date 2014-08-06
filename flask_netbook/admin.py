# Flask-Netbook Version 0.0.1
# Admin.py

from flask import Flask

from app import app, db, auth
from models import User, Note
from flask_turboduck.admin import Admin


admin = Admin(app, auth, branding='Example Site')
auth.register_admin(admin)
admin.register(Note)
admin.register(User)
admin.setup()

