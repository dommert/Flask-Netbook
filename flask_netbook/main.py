# Flask-Netbook Version 0.0.1
# Author: Dommert (Dommert@Gmail.com)
#

from app import app, db
from auth import *
from admin import admin
#from api import api
from models import *
from views import *



admin.setup()
#api.setup()


from flask_rum.main import rum
import flask_rum.rum_config as rum_config
app.config.from_object(rum_config)
app.config.THEME_FOLDER='rum/banana/'
app.register_blueprint(rum)


if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])

