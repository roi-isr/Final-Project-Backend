from .database import Database

CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS admins
                           (id SERIAL PRIMARY KEY,
                            username varchar(255),
                            password varchar(255))"""

INSERT_ADMIN_QUERY = "INSERT INTO admins VALUES (DEFAULT, %s, %s)"

DROP_TABLE_QUERY = """DROP TABLE IF EXISTS Admins"""


class AdminDatabase(Database):
    def __init__(self):
        super().__init__()

    # Create a table, getting its name and fields attributes
    def create_table(self):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(CREATE_TABLE_QUERY)

    # Insert data for table in the DB
    def add_admin(self, data):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(INSERT_ADMIN_QUERY,
                        (data[0], data[1]))

    def drop_table(self):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(DROP_TABLE_QUERY)
