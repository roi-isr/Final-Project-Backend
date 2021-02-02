
CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS contact
                        (email_address varchar(255) NOT NULL,
                         name varchar(255),
                         phone varchar(255),
                         content varchar(555),
                         create_at TIMESTAMP DEFAULT (now() at time zone 'utc-2'))"""

INSERT_DATA_QUERY = "INSERT INTO Contact VALUES (%s, %s, %s, %s, DEFAULT)"

GET_DATA_QUERY = """SELECT email_address,name,phone,content,create_at
                    FROM Contact
                    WHERE email_address=%s;"""

GET_DATA_ALL_QUERY = """SELECT email_address,name,phone,content,create_at
                        FROM Contact
                        ORDER BY create_at DESC;"""