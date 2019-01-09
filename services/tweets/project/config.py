# services/users/project/config.py
import os  # new

class BaseConfig:
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')