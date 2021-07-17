CREATE_ADVISE_MODEL_QUERY = """CREATE TABLE IF NOT EXISTS ml_advise
                        (create_at TIMESTAMP DEFAULT (now() at time zone 'utc-2') PRIMARY KEY,
                         model bytea NOT NULL,
                         scaler_X bytea NOT NULL,
                         scaler_y bytea NOT NULL,
                         accuracy real NOT NULL)"""

INSERT_ADVISE_MODEL_QUERY = """INSERT INTO ml_advise
                       VALUES (DEFAULT, %s, %s, %s, %s)
                       RETURNING create_at"""

DELETE_ALL_ADVISE_MODELS_QUERY = """TRUNCATE TABLE ml_advise"""

GET_ADVISE_MODEL_QUERY = """SELECT *
                     FROM ml_advise
                     LIMIT 1"""
