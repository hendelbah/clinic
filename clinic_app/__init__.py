from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from clinic_app.config import app_config


db = SQLAlchemy()
login_manager = LoginManager()
import clinic_app.models

def create_app(config_name):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    import clinic_app.models
    db.app = app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    Migrate(app, db)

    # from high_school import api
    # app.register_blueprint(api.api_bp, url_prefix='/api/v1')
    return app
