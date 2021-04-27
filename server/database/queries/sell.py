
CREATE_SELL_QUERY = """CREATE TABLE IF NOT EXISTS sell
                       (sell_id SERIAL PRIMARY KEY,
                        package_code varchar(50) NOT NULL,
                        package_model varchar(50) NOT NULL,
                        weight_in_carat REAL NOT NULL,
                        price_per_carat REAL NOT NULL,
                        buying_entity varchar(50) NOT NULL,
                        sell_date DATE NOT NULL,
                        payment_method varchar(255) NOT NULL)"""

INSERT_SELL_QUERY = """INSERT INTO sell
                          VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s)
                          RETURNING sell_id"""


GET_SELL_ALL_QUERY = """SELECT *
                         FROM sell
                         ORDER BY sell_date DESC"""

UPDATE_SELL_ITEM_QUERY = """UPDATE sell
                             SET ({})=%s
                             WHERE sell_id=%s
                             RETURNING sell_id"""

DELETE_SELL_ITEM = """DELETE FROM sell
                      WHERE sell_id=%s"""
