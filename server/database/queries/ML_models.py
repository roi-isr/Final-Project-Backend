CREATE_MODEL_QUERY = """CREATE TABLE IF NOT EXISTS ml_models
                        (create_at TIMESTAMP DEFAULT (now() at time zone 'utc-2') PRIMARY KEY,
                         model bytea NOT NULL,
                         scaler_X bytea NOT NULL,
                         scaler_y bytea NOT NULL)"""

INSERT_MODEL_QUERY = """INSERT INTO ml_models
                       VALUES (DEFAULT, %s, %s, %s)
                       RETURNING create_at"""

DELETE_ALL_MODELS_QUERY = """TRUNCATE TABLE ml_models"""

GET_MODEL_QUERY = """SELECT *
                     FROM ml_models
                     LIMIT 1"""
