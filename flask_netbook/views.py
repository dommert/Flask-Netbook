# Flask-Netbook Version 0.0.2
# Views.py

import datetime
from app import app
from auth import auth
from models import User, Note
from flask import request, redirect, url_for, render_template, flash
from flask_turboduck.utils import get_object_or_404, object_list

@app.route('/')
def front_index():
    return 'Frontpage'

@app.route('/notes/', methods=['GET','POST'])
def notes_index():
    if request.method == 'POST' and request.form['message']:
        user = auth.get_logged_in_user()
        message = Note.create(user=user, message=request.form['message'],)
        message.save()
        flash('You submited data!')
    return render_template('base_note.html')

@app.route('/note/<noteid>')
def note_view(noteid):
    return render_template('note.html')

@app.route('/note/add/')
def note_add():
    return 'Add a Note'

@app.route('/note/<noteid>/edit')
def note_edit(noteid):
    return 'Edit a note: ' +noteid

@app.route('/private/')
@auth.login_required
def private_timeline():
    user = auth.get_logged_in_user()

    return 'PRIVATE!'

@app.route('/users/')
def user_list():
    users = User.select().order_by(User.username)
    return object_list('user_list.html', users, 'user_list')

@app.route('/users/<username>/')
def user_detail(username):
    user = get_object_or_404(User, User.username==username)
    return user

@app.route('/login/')
def login():
    return redirect('/accounts/login/')