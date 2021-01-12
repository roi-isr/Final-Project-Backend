""" Defining a DB class, which implements a direct connection and action functions with the PostgreSQL DB"""

import psycopg2
from server.config_files.connection_config import CONNECTION_INFO


class Database:
    def __init__(self):
        self.connection = self.connect()

    @staticmethod
    # Create connection between the server and db
    def connect():
        connection = psycopg2.connect(CONNECTION_INFO)
        return connection

    # Close open connection with DB
    def close_connection(self):
        self.connection.close()
