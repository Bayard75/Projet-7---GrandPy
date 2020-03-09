from os import environ

class Config(object):
    DEBUG=False
    TESTING=False
    SESSION_COOKIE_SECURE=True
    FLASK_APP='grandpy.py'
    GOOGLE_API_KEY=str(environ.get('GOOGLE_API_KEY'))

class DevelopmentConfig(Config):
    DEBUG=True
    ENV='development'
