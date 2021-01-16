# from server.database.database import Database

CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS Contact
                        (email_address varchar(255) NOT NULL,
                         name varchar(255),
                         phone varchar(255),
                         content varchar(555),
                         create_at TIMESTAMP DEFAULT (now() at time zone 'utc-2'))"""

INSERT_DATA_QUERY = "INSERT INTO Contact VALUES (%s, %s, %s, %s, DEFAULT)"

GET_DATA_QUERY = """SELECT email_address,name,phone,content
                   FROM Contact
                   WHERE email_address=%s;"""
