"""
This module contains all configuration data for web application
"""
import pathlib
import os

BASE_DIR = pathlib.Path(__file__).parent
FLASK_CONFIG = os.getenv('FLASK_CONFIG')
DB_USER = os.getenv('FLASK_DB_USER')
DB_PASS = os.getenv('FLASK_DB_PASSWORD')
DB_SERVER = os.environ.get('FLASK_DB_SERVER')
DB_NAME = os.getenv('FLASK_DB_NAME')
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')


class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = FLASK_SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_SERVER}/clinic_test'
    TESTING = True
    SQLALCHEMY_ECHO = True
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_SERVER}/{DB_NAME}'
    DEBUG = False


config_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

CurrentConfig = config_name[FLASK_CONFIG]
