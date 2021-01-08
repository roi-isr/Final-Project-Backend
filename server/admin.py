""" Defining an admin class, used for further authentication process """

import psycopg2
from .config_files.connection_config import CONNECTION_INFO


class Admin:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = psycopg2.connect(CONNECTION_INFO)
        with connection as conn:
            cur = conn.cursor()
            query = "SELECT * FROM Admins WHERE username=%s"
            cur.execute(query, (username,))
        row = cur.fetchone()
        if row:
            admin = cls(*row)
        else:
            admin = None
        connection.close()
        return admin

    @classmethod
    def find_by_id(cls, _id):
        connection = psycopg2.connect(CONNECTION_INFO)
        with connection as conn:
            cur = conn.cursor()
            query = "SELECT * FROM Admins WHERE id=%s"
            cur.execute(query, (_id,))
        row = cur.fetchone()
        if row:
            admin = cls(*row)
        else:
            admin = None
        connection.close()
        return admin
