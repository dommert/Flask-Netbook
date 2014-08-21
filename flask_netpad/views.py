# Flask-Netpad Version 0.0.3
# Views.py

import datetime
from app import app
from auth import auth
from models import User, Note
from flask import request, redirect, url_for, render_template, flash
from flask_turboduck.utils import get_object_or_404, object_list

# Note List
@app.route('/note/', methods=['GET','POST'])
@app.route('/notes/', methods=['GET','POST'])
def note_list():
    user = auth.get_logged_in_user()
    notes = Note.select().where(Note.user == user).order_by(Note.created.desc())
    return object_list('note_list.html', notes, 'notes')

# Note View
@app.route('/note/<int:noteid>', methods=['GET','POST'])
def note_view(noteid):
    user = auth.get_logged_in_user() # Logged In User
    note = get_object_or_404(Note, Note.id==noteid, Note.user==user)
    return render_template('note_view.html', note=note)

# Note Add
@app.route('/note/add/', methods=['GET','POST'])
@auth.login_required
def note_add():
    if request.method == 'POST' and request.form['message']:
        user = auth.get_logged_in_user()
        message = Note.create(user=user, message=request.form['message'], title=request.form['title'],)
        message.save()
        flash('You submited data!')
        return redirect(url_for('note_list'))
    return render_template('note_add.html')

# Note Edit
@app.route('/note/<noteid>/edit', methods=['GET','POST'])
@auth.login_required
def note_edit(noteid):
    user = auth.get_logged_in_user() # Logged In User
    note = get_object_or_404(Note, Note.user==user, Note.id==noteid)
    if request.method == 'POST' and request.form['message']:
        note.message = request.form['message']
        note.title = request.form['title']
        note.save()
        flash('Thanks! You updated the data!')
        return redirect(url_for('note_list'))
    return render_template('note_edit.html', note=note)

# Private Area
@app.route('/private/')
@auth.login_required
def private_timeline():
    user = auth.get_logged_in_user()
    return 'PRIVATE!'

# User List
@app.route('/users/')
def user_list():
    users = User.select().order_by(User.username)
    return object_list('user_list.html', users, 'user_list')

# User View
@app.route('/users/<username>/')
def user_detail(username):
    user = get_object_or_404(User, User.username==username)
    return user

# Login Page
@app.route('/login/')
def login():
    return redirect('/accounts/login/')