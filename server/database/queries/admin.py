
CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS admins
                           (id SERIAL PRIMARY KEY,
                            username varchar(255),
                            password varchar(50))"""

INSERT_ADMIN_QUERY = """INSERT INTO admins 
                        VALUES (DEFAULT, %s, %s)
                        RETURNING id"""

DROP_TABLE_QUERY = """DROP TABLE IF EXISTS Admins"""

DELETE_ADMIN_ITEM = """DELETE FROM admin
                       WHERE id=%s"""
