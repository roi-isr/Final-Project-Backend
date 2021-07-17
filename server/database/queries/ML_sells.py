CREATE_SELLS_MODEL_QUERY = """CREATE TABLE IF NOT EXISTS ml_sells
                              (create_at TIMESTAMP DEFAULT (now() at time zone 'utc-2') PRIMARY KEY,
                               model bytea NOT NULL,
                               scaler_X bytea NOT NULL,
                               scaler_y bytea NOT NULL,
                               accuracy real NOT NULL)"""

CREATE_SELL_DATA_QUERY = """CREATE TABLE IF NOT EXISTS sells_data
                            (_id SERIAL PRIMARY KEY,
                             weight_in_carat REAL NOT NULL,
                             sell_price REAL NOT NULL,
                             clarity varchar(50),
                             color varchar(50))"""

INSERT_SELLS_MODEL_QUERY = """INSERT INTO ml_sells
                            VALUES (DEFAULT, %s, %s, %s)
                            RETURNING create_at"""

INSERT_SELL_DATA_QUERY = """INSERT INTO sells_data
                            VALUES (DEFAULT, %s, %s, %s, %s)
                            RETURNING _id"""

RESET_SELLS_MODEL_QUERY = """TRUNCATE TABLE sells_data"""

GET_SELLS_DATA_QUERY = """SELECT weight_in_carat, color, clarity, sell_price
                          FROM sells_data"""

GET_SELLS_COUNT_QUERY = """SELECT count(*)
                          FROM sells_data"""

GET_SELLS_MODEL_QUERY = """SELECT *
                     FROM ml_sells
                     LIMIT 1"""

INSERT_SELLS_MODEL_QUERY = """INSERT INTO ml_sells
                               VALUES (DEFAULT, %s, %s, %s, %s)
                               RETURNING create_at"""

DELETE_ALL_SELLS_MODELS_QUERY = """TRUNCATE TABLE sells_data"""
