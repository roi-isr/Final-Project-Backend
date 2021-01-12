from .database import Database

CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS Contact
                        (email_address varchar(255) NOT NULL,
                         name varchar(255),
                         phone varchar(255),
                         content varchar(555))"""

INSERT_DATA_QUERY = "INSERT INTO Contact VALUES (%s, %s, %s,%s)"

GET_DATA_QUERY = """SELECT email_address,name,phone,content
                   FROM Contact
                   WHERE email_address=%s;"""


class ContactDatabase(Database):
    def __init__(self):
        super().__init__()

    # Create a table, getting its name and fields attributes
    def create_table(self):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(CREATE_TABLE_QUERY)

    # Insert data for table in the DB
    def insert_data(self, data):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(INSERT_DATA_QUERY,
                        (data[0], data[1], data[2], data[3]))

    # Retrieve data from DB
    def get_data(self, email):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(GET_DATA_QUERY, (email,))
            return cur.fetchall()
