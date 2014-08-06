# Flask-Netbook Version 0.0.1
# Admin.py

from flask import Flask

from app import app, db, auth
from models import Note, User
from flask_turboduck.admin import Admin, ModelAdmin


# Admin Models

class MessageAdmin(ModelAdmin):
    columns = ('user', 'content', 'pub_date',)
    foreign_key_lookups = {'user': 'username'}

class UserAdmin(ModelAdmin):
    columns = ('username', 'email', 'is_superuser',)




# Register
admin = Admin(app, db)
admin.register(Note)
admin.register(User, UserAdmin)
admin.setup()


