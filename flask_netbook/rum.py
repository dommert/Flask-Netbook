from app import app
from flask_rum.main import rum
import flask_rum.rum_config as rum_config
app.config.from_object(rum_config)
app.config.THEME_FOLDER='rum/banana/'
app.register_blueprint(rum)
