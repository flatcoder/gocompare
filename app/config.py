import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Development(object):
    SECRET_KEY = "gocompare-coding-challenge-dev"
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'db/dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Testing(object):
    SECRET_KEY = "gocompare-coding-challenge-tdd"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'db/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Production(object):
    SECRET_KEY = "gocompare-coding-challenge-live"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'db/prod.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': Development,
    'production': Production,
    'test': Testing,
}
