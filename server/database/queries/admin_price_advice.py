CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS admin_advise
                        (advise_id SERIAL PRIMARY KEY, 
                         weight real NOT NULL,
                         cut varchar(50) NOT NULL,
                         color varchar(50) NOT NULL,
                         clarity varchar(50) NOT NULL,
                         table1 real NOT NULL,
                         depth real NOT NULL,
                         price real NOT NULL,
                         advised_price real NOT NULL)"""

INSERT_ADVISE_QUERY = """INSERT INTO admin_advise
                         VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
                         RETURNING advise_id"""

GET_ADVISE_ALL_QUERY = """SELECT weight, cut, clarity, color, table1, depth, price, advised_price
                          FROM admin_advise"""
