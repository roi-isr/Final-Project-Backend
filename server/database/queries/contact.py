# from server.database.database import Database

CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS Contact
                        (email_address varchar(255) NOT NULL,
                         name varchar(255),
                         phone varchar(255),
                         content varchar(555))"""

INSERT_DATA_QUERY = "INSERT INTO Contact VALUES (%s, %s, %s,%s)"

GET_DATA_QUERY = """SELECT email_address,name,phone,content
                   FROM Contact
                   WHERE email_address=%s;"""


# class ContactDatabase(Database):
#     def __init__(self):
#         super().__init__()
#
#     # Create a table, getting its name and fields attributes
#     def __create_table(self):
#         super().create_table(CREATE_TABLE_QUERY)
#
#     # Insert data for table in the DB
#     def __insert_data(self, data):
#         super().insert_data(INSERT_DATA_QUERY, data)
#
#     # Retrieve data from DB
#     def __get_specific_data(self, email):
#         super().get_specific_data(GET_DATA_QUERY, (email,))
#
