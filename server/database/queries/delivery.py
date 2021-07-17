CREATE_DELIVERY_QUERY = """CREATE TABLE IF NOT EXISTS delivery
                           (delivery_id SERIAL PRIMARY KEY,
                            package_code varchar(255) NOT NULL,
                            package_weight REAL,
                            delivery_from_country varchar(255),
                            delivery_company varchar(255),
                            sender varchar(255),
                            send_date DATE,
                            history BOOLEAN)"""

INSERT_DELIVERY_QUERY = """INSERT INTO delivery 
                           VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, FALSE)
                           RETURNING delivery_id"""

GET_DELIVERY_ALL_QUERY = """SELECT *
                            FROM delivery
                            WHERE history = FALSE
                            ORDER BY send_date DESC"""

GET_DELIVERY_HISTORY_QUERY = """SELECT *
                            FROM delivery
                            WHERE history = TRUE
                            ORDER BY send_date DESC"""

UPDATE_DELIVERY_ITEM_QUERY = """UPDATE delivery
                             SET ({})=%s
                             WHERE delivery_id=%s
                             RETURNING delivery_id"""

MOVE_TO_HISTORY_QUERY = """UPDATE delivery
                             SET history=TRUE
                             WHERE delivery_id=%s
                             RETURNING delivery_id"""

DELETE_DELIVERY_ITEM = """DELETE FROM delivery
                          WHERE delivery_id=%s"""

DROP_TABLE_QUERY = """DROP TABLE IF EXISTS delivery"""
