"""setting up a basic configuration for functionality
and data storage in a basic file"""
import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

#setting sql lite environment on data development configuration
#disables tracking of modifications
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    SQLALCHEMY_TRACK_MODIFICATION = False

config = {
    'development':DevelopmentConfig,
    'default': DevelopmentConfig
}
