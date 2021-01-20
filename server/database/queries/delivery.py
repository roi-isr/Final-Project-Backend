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
