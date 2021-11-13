import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')