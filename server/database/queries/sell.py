
CREATE_SELL_QUERY = """CREATE TABLE IF NOT EXISTS sell
                       (sell_id SERIAL PRIMARY KEY,
                        package_code varchar(50) NOT NULL,
                        package_model varchar(50) NOT NULL,
                        weight_in_carat REAL NOT NULL,
                        price_per_carat REAL NOT NULL,
                        buying_customer varchar(50),
                        customer_phone varchar(50),
                        customer_mail varchar(50),
                        sell_date DATE NOT NULL,
                        payment_method varchar(255) NOT NULL)"""

INSERT_SELL_QUERY = """INSERT INTO sell
                       VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                       RETURNING sell_id"""


GET_SELL_ALL_QUERY = """SELECT sell_id, package_code, package_model, weight_in_carat, price_per_carat, buying_customer,
                        sell_date, payment_method
                        FROM sell
                        ORDER BY sell_date DESC"""

GET_PREV_WEIGHT_QUERY = """SELECT weight_in_carat
                           FROM sell
                           WHERE sell_id=%s"""

GET_CUSTOMER_QUERY = """SELECT buying_customer, customer_mail, customer_phone
                        FROM sell
                        WHERE sell_id=%s"""

UPDATE_SELL_ITEM_QUERY = """UPDATE sell
                             SET ({})=%s
                             WHERE sell_id=%s
                             RETURNING sell_id"""

DELETE_SELL_ITEM = """DELETE FROM sell
                      WHERE sell_id=%s"""
