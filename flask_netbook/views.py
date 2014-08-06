# Flask-Netbook Version 0.0.1
# Views.py

# Flask
from flask import Flask
from flask import url_for, redirect
from flask import render_template, flash
# Netbook
from app import app


@app.route('/notes/', methods=['GET','POST'])
def notes():
    return 'Notes'

@app.route