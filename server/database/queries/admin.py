# from server.database.database import Database

CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS admins
                           (id SERIAL PRIMARY KEY,
                            username varchar(255),
                            password varchar(255))"""

INSERT_ADMIN_QUERY = "INSERT INTO admins VALUES (DEFAULT, %s, %s)"

DROP_TABLE_QUERY = """DROP TABLE IF EXISTS Admins"""
