"""
This module contains all configuration data for web application
"""
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

FLASK_CONFIG = os.getenv('FLASK_CONFIG', default='production')
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY', default='super-secret')

MYSQL_USER = os.getenv('FLASK_DB_USER', default='root')
MYSQL_PASSWORD = os.getenv('FLASK_DB_PASSWORD', default='')
MYSQL_SERVER = os.environ.get('FLASK_DB_SERVER', default='localhost')
MYSQL_DATABASE = os.getenv('FLASK_DB_NAME', default='clinic')


class Config:
    """
    Common configurations
    """
    SECRET_KEY = FLASK_SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}'
                               f'@{MYSQL_SERVER}/{MYSQL_DATABASE}?charset=utf8mb4')


class TestingConfig(Config):
    """
    Configuration for running tests.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
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
    API_KEY = 'qwerty'
    TESTING = True
    SQLALCHEMY_ECHO = True
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    API_KEY = '9T5vOAnb2tDGnRuxh2fhIabi2CIfvtWmi6MrUCNumxHRytuLNZKzd2zxtawQsprV'
    DEBUG = False


config_name = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

CurrentConfig = config_name[FLASK_CONFIG]
