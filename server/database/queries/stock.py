
CREATE_STOCK_QUERY = """CREATE TABLE IF NOT EXISTS stock
                          (stock_id SERIAL PRIMARY KEY,
                           package_model varchar(50) NOT NULL,
                           weight_in_karat real NOT NULL,
                           cost_per_karat real NOT NULL,
                           clearance varchar(50) NOT NULL,
                           color varchar(50) NOT NULL,
                           code varchar(50) NOT NULL,                           
                           comments varchar(255),                           
                           sell_date DATE,
                           status varchar(50) NOT NULL)"""

INSERT_STOCK_QUERY = """INSERT INTO diamond_package 
                          VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

GET_STOCK_ALL_QUERY = """SELECT *
                           FROM diamond_package"""

GET_STOCK_QUERY_BY_ID = """SELECT *
                             FROM diamond_package
                             WHERE package_code=%s"""

DELETE_STOCK_ITEM = """DELETE FROM diamond_package
                         WHERE stock_id=%s"""
