"""
This module contains all configuration data for web application
"""
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
FLASK_CONFIG = os.getenv('FLASK_CONFIG', default='development')
DB_USER = os.getenv('FLASK_DB_USER', default='root')
DB_PASS = os.getenv('FLASK_DB_PASSWORD', default='')
DB_SERVER = os.environ.get('FLASK_DB_SERVER', default='localhost')
DB_NAME = os.getenv('FLASK_DB_NAME', default='clinic_test')
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY', default='super-secret')


class Config:
    """
    Common configurations
    """
    SECRET_KEY = FLASK_SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    Configuration for running tests.
    """
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_SERVER}/clinic_test'
    API_KEY = 'qwerty'
    TESTING = True
    SQLALCHEMY_ECHO = False
    DEBUG = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_SERVER}/clinic_test' \
                              '?charset=utf8mb4'
    API_KEY = 'qwerty'
    TESTING = True
    SQLALCHEMY_ECHO = True
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_SERVER}/{DB_NAME}' \
                              '?charset=utf8mb4'
    API_KEY = '9T5vOAnb2tDGnRuxh2fhIabi2CIfvtWmi6MrUCNumxHRytuLNZKzd2zxtawQsprV'
    DEBUG = False


config_name = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

CurrentConfig = config_name[FLASK_CONFIG]
