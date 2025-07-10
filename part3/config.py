"""setting up a basic configuration for functionality
and data storage in a basic file"""
import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'develpoment':DevelopmentConfig,
    'default': DevelopmentConfig
}
