CREATE_SELLS_MODEL_QUERY = """CREATE TABLE IF NOT EXISTS ml_sells
                        (create_at TIMESTAMP DEFAULT (now() at time zone 'utc-2') PRIMARY KEY,
                         model bytea NOT NULL,
                         scaler_X bytea NOT NULL,
                         scaler_y bytea NOT NULL)"""

CREATE_SELL_ATTR_QUERY = """CREATE TABLE IF NOT EXISTS sells_attr
                            (_id SERIAL PRIMARY KEY,
                             weight_in_carat REAL NOT NULL,
                             sell_price REAL NOT NULL,
                             clarity varchar(50),
                             color varchar(50),
                             number_of_requests INTEGER)"""

INSERT_SELLS_MODEL_QUERY = """INSERT INTO ml_sells
                       VALUES (DEFAULT, %s, %s, %s)
                       RETURNING create_at"""

INSERT_SELL_ATTR_QUERY = """INSERT INTO sells_attr
                       VALUES (DEFAULT, %s, %s, %s, %s, %s)
                       RETURNING _id"""
