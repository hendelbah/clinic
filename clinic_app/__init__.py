"""
Package stores all source files of project.
This module provides create_app function for initializing Flask-Application
"""
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, has_request_context, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from clinic_app.config import app_config


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()


def create_app(config_name):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    conf = app_config[config_name]
    app.config.from_object(conf)
    # import clinic_app.models
    db.app = app
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    request_formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
        '%(levelname)s in %(module)s: %(message)s'
    )
    file_handler = RotatingFileHandler(
        conf.BASE_DIR / 'logs' / 'clinic.log', maxBytes=10240, backupCount=10
    )
    file_handler.setFormatter(request_formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('App startup')

    from rest import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
