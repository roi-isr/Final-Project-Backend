""" Defining a DB class, which implements a direct connection and action functions with the PostgreSQL DB"""

import psycopg2
from .config_files.connection_config import CONNECTION_INFO


class DB:
    def __init__(self):
        self.connection = self.connect_db()

    @staticmethod
    # Create connection between the server and db
    def connect_db():
        connection = psycopg2.connect(CONNECTION_INFO)
        return connection

    # Create a table, getting its name and fields attributes
    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS Contact
                        (email_address varchar(255) NOT NULL,
                         name varchar(255),
                         phone varchar(255),
                         content varchar(555))"""
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query)

    # Create a table, getting its name and fields attributes
    def create_admin_table(self):
        query = """CREATE TABLE IF NOT EXISTS Admins
                        (id SERIAL,
                         username varchar(255),
                         password varchar(255))"""
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query)

    # Insert data for table in the DB
    def insert_data(self, data):
        query = "INSERT INTO Contact VALUES (%s, %s, %s,%s)"
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query, (data[0], data[1], data[2], data[3]))

    # Insert data for table in the DB
    def add_admin(self, data):
        query = "INSERT INTO Admins VALUES (DEFAULT, %s, %s)"
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query, (data[0], data[1]))

    # Retrieve data from DB
    def get_data(self, email):
        query = """SELECT email_address,name,phone,content
                   FROM Contact
                   WHERE email_address=%s;"""
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query, (email,))
            return cur.fetchall()


    def drop_admin_table(self):
        query = """DROP TABLE IF EXISTS Admins"""
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query)

    # Close open connection with DB
    def close_connection(self):
        self.connection.close()
