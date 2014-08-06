# Flask-Netbook Version 0.0.1
# configs.py

class Configuration(object):
    DATABASE = {
        'name': 'flask_netbook.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    DEBUG = True
    SECRET_KEY = 'shhhhh!!!'