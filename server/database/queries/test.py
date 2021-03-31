CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS test
                        (create_at TIMESTAMP DEFAULT (now() at time zone 'utc-2'),
                         test_message varchar(50) NOT NULL)"""
ADD_QUERY = """INSERT INTO test
               VALUES (DEFAULT, %s)
               RETURNING create_at"""
