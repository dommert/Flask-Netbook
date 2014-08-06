# Flask-Netbook Version 0.0.1
# Author: Dommert (Dommert@Gmail.com)
#

# Flask
from flask import Flask, Blueprint
# Flask-Rum
from flask_rum.main import rum
# Netbook
from app import app
from views import *
import models



#Import in Rum Configs
import flask_rum.rum_config as rum_config
app.config.from_object(rum_config)
# Sample override of Theme
app.config.THEME_FOLDER='rum/banana/'


if __name__ == '__main__':
    app.register_blueprint(rum) #  Flask-Rum Blueprint
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])

