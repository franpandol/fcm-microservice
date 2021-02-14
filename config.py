import os


class BaseConfig(object):
    DEBUG = True
    DEVELOPMENT = True


class ProductionConfig(BaseConfig):
    DEVELOPMENT = False
    DEBUG = False
    CLIENT_API_KEY = os.environ.get('CLIENT_API_KEY')
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
