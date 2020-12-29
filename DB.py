import psycopg2
from config import CONNECTION_INFO


class DB:
    def __init__(self):
        self.connction = self.connect_db()

    # Create connection between the server and db
    def connect_db(self):
        connection = psycopg2.connect(CONNECTION_INFO)
        return connection

    # Create a table, getting its name and fields attributes
    def create_table(self):
        with self.connction as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Contact
                        (email_address varchar(255) NOT NULL,
                         name varchar(255),
                         phone varchar(255),
                         content varchar(555))""")

    # Create a table, getting its name and fields attributes
    def create_admin_table(self):
        with self.connction as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Admins
                        (id SERIAL,
                         username varchar(255),
                         password varchar(255))""")

    # insert data for table in the DB
    def insert_data(self, data):
        with self.connction as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Contact VALUES (%s, %s, %s,%s)",
                        (data[0], data[1], data[2], data[3]))

    # Insert data for table in the DB
    def add_admin(self, data):
        with self.connction as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Admins VALUES (DEFAULT, %s, %s)",
                        (data[0], data[1]))

    # retrieve data from DB
    def get_data(self, email):
        with self.connction as conn:
            cur = conn.cursor()
            cur.execute("""SELECT email_address,name,phone,content
                           FROM Contact
                           WHERE email_address=%s;""",
                        (email,))
            return cur.fetchall()

    def close_connection(self):
        self.connction.close()
