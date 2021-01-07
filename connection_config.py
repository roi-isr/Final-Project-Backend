""" Connection configuration file """
import os
CONNECTION_INFO = ""
try:
    from connection_secret import CONNECTION_SECRET
    CONNECTION_INFO = CONNECTION_SECRET
except ModuleNotFoundError:
    CONNECTION_INFO = os.environ['DATABASE_URL']
