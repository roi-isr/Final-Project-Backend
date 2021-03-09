
CREATE_SELL_QUERY = """CREATE TABLE IF NOT EXISTS sell
                       (sell_id SERIAL PRIMARY KEY,
                        package_code varchar(255) NOT NULL REFERENCES diamond_package(package_code),
                        price real NOT NULL,
                        buying_company varchar(255) NOT NULL,
                        mediator_name varchar(255))"""

INSERT_SELL_QUERY = """INSERT INTO sell 
                          VALUES (DEFAULT, %s, %s, %s, %s)
                          RETURNING sell_id"""

GET_SELL_ALL_QUERY = """SELECT sell.*, diamond_package.weight_in_karat
                        FROM sell
                        INNER JOIN diamond_package
                        ON sell.package_code = diamond_package.package_code
                        WHERE diamond_package.status = 'SOLD'"""

GET_SELL_QUERY_BY_CODE = """SELECT sell.*, diamond_package.weight_in_karat
                            FROM sell
                            INNER JOIN diamond_package
                            ON sell.package_code = diamond_package.package_code
                            WHERE diamond_package.status = 'SOLD' and diamond_package.package_code = %s"""

DELETE_SELL_ITEM = """DELETE FROM SELL
                      WHERE package_code=%s"""
