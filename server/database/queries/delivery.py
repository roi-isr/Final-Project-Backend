
CREATE_DELIVERY_QUERY = """CREATE TABLE IF NOT EXISTS delivery
                           (delivery_id SERIAL PRIMARY KEY,
                            package_code varchar(255) NOT NULL REFERENCES diamond_package(package_code),
                            delivery_company varchar(255),
                            delivery_origin varchar(255))"""

INSERT_DELIVERY_QUERY = """INSERT INTO delivery 
                           VALUES (DEFAULT, %s, %s, %s)"""

GET_DELIVERY_ALL_QUERY = """SELECT delivery.*, diamond_package.seller
                            FROM delivery
                            INNER JOIN diamond_package
                            ON delivery.package_code = diamond_package.package_code
                            WHERE diamond_package.status = 'ON_DELIVERY'"""

DELETE_DELIVERY_ITEM = """DELETE FROM delivery
                          WHERE delivery_id=%s"""

DROP_TABLE_QUERY = """DROP TABLE IF EXISTS delivery"""
