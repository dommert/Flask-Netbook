# Flask-Netpad Version 0.0.3
# config.py

class Configuration(object):
    DATABASE = {
        'name': 'flask_netbook.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    HOST = '0.0.0.0'
    PORT = 5001
    DEBUG = True
    SECRET_KEY = 'shhhhh!!!'