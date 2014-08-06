# Flask-Netbook Version 0.0.1
# Views.py

# Flask
from flask import Flask
from flask import url_for, redirect
from flask import render_template, flash
# Netbook
from app import app


@app.route('/')
def front_index():
    return 'Frontpage'

@app.route('/notes/', methods=['GET','POST'])
def notes_list():
    return 'Notes'

@app.route('/note/<noteid>')
def note_view(noteid):
    return 'View a Note'

@app.route('/note/add/')
def note_add():
    return 'Add a Note'

@app.route('note/<noteid>/edit')
def note_edit(noteid):
    return 'Edit a note'



