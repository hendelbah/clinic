"""
This module contains all configuration data for web application
"""
import pathlib
import os

BASE_DIR = pathlib.Path(__file__).parent
DB_USER = os.getenv('FLASK_DB_USER')
DB_PASS = os.getenv('FLASK_DB_PASSWORD')
DB_NAME = os.getenv('FLASK_DB_NAME')


class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@localhost/clinic_test'
    TESTING = True
    SQLALCHEMY_ECHO = True
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}'
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
