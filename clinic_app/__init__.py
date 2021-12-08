"""
Package stores all source files of project.
This module stands for app initialization and configuring
"""
import logging
import sys
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from clinic_app.config import CurrentConfig, BASE_DIR

app = Flask(__name__)
app.config.from_object(CurrentConfig)

db = SQLAlchemy(app)
ma = Marshmallow(app)

migration = Migrate(app, db, directory=BASE_DIR / 'migrations')

login_manager = LoginManager(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
log_path = BASE_DIR / 'logs' / 'clinic.log'
file_handler = RotatingFileHandler(log_path, maxBytes=1048576, backupCount=10)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# pylint: disable=no-member
logger = app.logger
logger.handlers.clear()
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)
logger.info('App initialization')
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(console_handler)
werkzeug_logger.setLevel(logging.INFO)

# pylint: disable=cyclic-import,wrong-import-position
from clinic_app.rest import api_blueprint

app.register_blueprint(api_blueprint)
