"""
Package stores all source files of project.
This module stands for app initialization and configuring
"""
import sys
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from clinic_app.config import CurrentConfig, BASE_DIR

app = Flask(__name__)
app.config.from_object(CurrentConfig)
print(CurrentConfig.SQLALCHEMY_DATABASE_URI)
db = SQLAlchemy(app)
ma = Marshmallow(app)

migration = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
log_path = BASE_DIR / 'logs' / 'clinic.log'
file_handler = RotatingFileHandler(log_path, maxBytes=10240, backupCount=10)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

app.logger.handlers.clear()
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)
app.logger.setLevel(logging.DEBUG)
app.logger.info('App initialization')
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(console_handler)
werkzeug_logger.setLevel(logging.DEBUG)

from clinic_app.rest import api_blueprint

app.register_blueprint(api_blueprint)
