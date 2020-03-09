from os import environ

class Config(object):
    '''This class is the default config for FLASK'''

    DEBUG=False
    TESTING=False
    SESSION_COOKIE_SECURE=True
    FLASK_APP='grandpy.py'
    GOOGLE_API_KEY=(environ.get('GOOGLE_API_KEY'))

class DevelopmentConfig(Config):
    '''Class handling the development env'''
    DEBUG=True
    ENV='development'
