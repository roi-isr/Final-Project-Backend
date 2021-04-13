""" Connection configuration file """
import os
CONNECTION_INFO = ""
try:
    from .connection_secret import CONNECTION_SECRET, DATABASE_URL_PATH
    CONNECTION_INFO = CONNECTION_SECRET
    DATABASE_URL = DATABASE_URL_PATH
except ModuleNotFoundError:
    CONNECTION_INFO = os.environ['DATABASE_URL']
    DATABASE_URL = os.environ['DATABASE_URL_FIXED']
