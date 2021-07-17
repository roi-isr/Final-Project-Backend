CREATE_STOCK_QUERY = """CREATE TABLE IF NOT EXISTS stock
                        (stock_id SERIAL PRIMARY KEY,
                         package_model varchar(50) NOT NULL,
                         weight_in_karat real NOT NULL,
                         cost_per_karat real NOT NULL,
                         clearance varchar(50) NOT NULL,
                         color varchar(50) NOT NULL,
                         code varchar(50) NOT NULL UNIQUE,                           
                         comments varchar(255),                           
                         sell_date DATE,
                         cost_per_sell real NOT NULL,
                         status varchar(50) NOT NULL)"""

SELECT_STORE_STOCK = """SELECT weight_in_karat
                        FROM stock
                        WHERE code=%s"""

UPDATE_STORE_STOCK = """UPDATE stock
                             SET weight_in_karat=weight_in_karat-CAST(%s AS REAL)
                             WHERE code=%s
                             RETURNING stock_id"""

INSERT_STOCK_QUERY = """INSERT INTO stock 
                        VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING stock_id"""

GET_STOCK_ALL_QUERY = """SELECT *
                         FROM stock
                         ORDER BY sell_date DESC"""

GET_STOCK_ALL_QUERY = """SELECT *
                         FROM stock
                         ORDER BY sell_date DESC"""

GET_STOCK_QUERY_BY_ID = """SELECT *
                           FROM stock
                           WHERE package_code=%s"""

UPDATE_STOCK_ITEM_QUERY = """UPDATE stock
                             SET ({})=%s
                             WHERE stock_id=%s
                             RETURNING stock_id"""

UPDATE_STOCK_STATUS_QUERY = """UPDATE stock
                               SET status=%s
                               WHERE stock_id=%s
                               RETURNING stock_id"""

DELETE_STOCK_ITEM = """DELETE FROM stock
                       WHERE stock_id=%s"""

STOCK_TO_OFFER_ALL_QUERY = """SELECT stock.stock_id, COUNT(*)
                              FROM stock INNER JOIN offer
                              ON stock.stock_id=offer.package_id
                              GROUP BY stock.stock_id"""

STOCK_TO_OFFER_ONE_QUERY = """SELECT offer.offer_id, stock.stock_id, stock.package_model, stock.code, offer.name,
                                     offer.phone, offer.email, offer.offered_weight, offer.offered_price, 
                                     offer.additional_comments, offer.create_at
                                     FROM stock INNER JOIN offer
                                     ON stock.stock_id=offer.package_id
                                     WHERE stock.stock_id=%s
                                     ORDER BY offer.create_at ASC"""

GET_STOCK_ID_QUERY = """SELECT stock_id
                        FROM stock
                        WHERE code=%s"""

DELETE_RELATED_OFFERS_QUERY = """DELETE FROM offer
                                 WHERE package_id=%s"""
