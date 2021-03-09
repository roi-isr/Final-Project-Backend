
CREATE_DELIVERY_QUERY = """CREATE TABLE IF NOT EXISTS delivery
                           (delivery_id SERIAL PRIMARY KEY,
                            package_code varchar(255) NOT NULL,
                            package_weight REAL,
                            delivery_from_country varchar(255),
                            delivery_company varchar(255),
                            sender varchar(255),
                            send_date DATE)"""

#REFERENCES diamond_package(package_code)
# , diamond_package.seller

INSERT_DELIVERY_QUERY = """INSERT INTO delivery 
                           VALUES (DEFAULT, %s, %s, %s, %s, %s, %s)
                           RETURNING delivery_id"""

GET_DELIVERY_ALL_QUERY = """SELECT *
                            FROM delivery"""


DELETE_DELIVERY_ITEM = """DELETE FROM delivery
                          WHERE delivery_id=%s"""

DROP_TABLE_QUERY = """DROP TABLE IF EXISTS delivery"""
