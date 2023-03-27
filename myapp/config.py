import os
from sqlalchemy import create_engine

class config(object):
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COOKIE_SECURE=False

class DevelopmenConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@127.0.0.1/my_essence'
    SQLALCHEMY_TRACK_MODIDICATION=False