# from server.database.database import Database

CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS admins
                           (id SERIAL PRIMARY KEY,
                            username varchar(255),
                            password varchar(255))"""

INSERT_ADMIN_QUERY = "INSERT INTO admins VALUES (DEFAULT, %s, %s)"

DROP_TABLE_QUERY = """DROP TABLE IF EXISTS Admins"""


# class AdminDatabase(Database):
#     def __init__(self):
#         super().__init__()
#
#     # Create a table, getting its name and fields attributes
#     def __create_table(self):
#         super().create_table(CREATE_TABLE_QUERY)
#
#     # Insert data for table in the DB
#     def __insert_data(self, data):
#         super().insert_data(INSERT_ADMIN_QUERY, data)
#
#     def __drop_table(self):
#         super().drop_table(DROP_TABLE_QUERY)
