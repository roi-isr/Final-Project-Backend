# from server.database.database import Database

CREATE_DELIVERY_QUERY = """CREATE TABLE IF NOT EXISTS delivery
                           (delivery_id SERIAL PRIMARY KEY,
                            package_code varchar(255) REFERENCES diamond_package
                            delivery_company varchar(255),
                            delivery_origin varchar(255),
                            seller varchar(255)"""

INSERT_DELIVERY_QUERY = """INSERT INTO admins 
                           VALUES (DEFAULT, %s, %s, %s, %s)"""

GET_DELIVERY_ALL_QUERY = """SELECT *
                            FROM delivery"""

DELETE_DELIVERY_ITEM = """DELETE FROM delivery
                          WHERE delivery_id=%s"""

DROP_TABLE_QUERY = """DROP TABLE IF EXISTS delivery"""


# class ContactDatabase(Database):
#     def __init__(self):
#         super().__init__()
#
#     # Create a table, getting its name and fields attributes
#     def __create_table(self):
#         super().create_table(CREATE_DELIVERY_QUERY)
#
#     # Insert data for table in the DB
#     def __insert_data(self, data):
#         super().insert_data(INSERT_DELIVERY_QUERY, data)
#
#     # Retrieve data from DB
#     def __get_all_data(self):
#         super().get_all_data(GET_DELIVERY_ALL_QUERY)
#
#     def __delete_item(self, item_id):
#         super().delete_item(DELETE_DELIVERY_ITEM, (item_id,))
#
#     def __drop_table(self):
#         super().drop_table(DROP_TABLE_QUERY)
#
