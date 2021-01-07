""" Connection configuration file """
import os
from connection_secret import CONNECTION_SECRET


CONNECTION_INFO = os.environ['DATABASE_URL']
if not CONNECTION_INFO:
    CONNECTION_INFO = CONNECTION_SECRET
