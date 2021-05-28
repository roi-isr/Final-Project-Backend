CREATE_ADVICE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS admin_advise
                        (advise_id SERIAL PRIMARY KEY, 
                         weight real NOT NULL,
                         cut varchar(50) NOT NULL,
                         color varchar(50) NOT NULL,
                         clarity varchar(50) NOT NULL,
                         depth real NOT NULL,
                         table1 real NOT NULL,
                         advised_price real NOT NULL)"""

INSERT_ADVISE_QUERY = """INSERT INTO admin_advise
                         VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s)
                         RETURNING advise_id"""

GET_ADVISE_ALL_QUERY = """SELECT weight, cut, color, clarity, depth, table1, advised_price
                          FROM admin_advise"""

GET_ITEMS_COUNTER_QUERY = """SELECT count(*)
                             FROM admin_advise"""

RESET_ADVISE_MODEL_QUERY = """TRUNCATE TABLE admin_advise"""
