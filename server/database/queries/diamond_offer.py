
CREATE_OFFER_QUERY = """CREATE TABLE IF NOT EXISTS offer
                        (offer_id SERIAL PRIMARY KEY,
                         package_id int REFERENCES stock(stock_id),
                         name varchar(50) NOT NULL,
                         phone varchar(50) NOT NULL,
                         email varchar(255) NOT NULL,
                         offered_weight REAL NOT NULL,
                         offered_price REAL NOT NULL,
                         additional_comments varchar(255),
                         create_at TIMESTAMP DEFAULT (now() at time zone 'utc-2'))"""

INSERT_OFFER_QUERY = """INSERT INTO offer
                       VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, DEFAULT)
                       RETURNING offer_id"""

GET_SPECIFIC_OFFER_QUERY = """SELECT *
                              FROM offer
                              where offer_id=%s"""

UPDATE_OFFER_ITEM_QUERY = """UPDATE offer
                             SET ({})=%s
                             WHERE offer_id=%s
                             RETURNING offer_id"""

DELETE_OFFER_ITEM = """DELETE FROM offer
                      WHERE offer_id=%s"""