
CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS contact
                        (id SERIAL PRIMARY KEY, 
                         email_address varchar(255) NOT NULL,
                         name varchar(255),
                         phone varchar(255),
                         content varchar(555),
                         create_at TIMESTAMP DEFAULT (now() at time zone 'utc-2'))"""

INSERT_CONTACT_QUERY = "INSERT INTO Contact VALUES (DEFAULT, %s, %s, %s, %s, DEFAULT)"

GET_CONTACT_QUERY = """SELECT id, email_address,name,phone,content,create_at
                    FROM Contact
                    WHERE email_address=%s;"""

GET_CONTACT_ALL_QUERY = """SELECT id, email_address,name,phone,content,create_at
                        FROM Contact
                        ORDER BY create_at DESC;"""

DELETE_CONTACT_ITEM = """DELETE FROM contact
                       WHERE id=%s"""
