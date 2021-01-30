
CREATE_PACKAGE_QUERY = """CREATE TABLE IF NOT EXISTS diamond_package
                          (package_code varchar(255) NOT NULL PRIMARY KEY,
                           weight_in_karat real NOT NULL,
                           cost_per_karat real NOT NULL,
                           clearance varchar(255) NOT NULL,
                           color varchar(255) NOT NULL,
                           seller varchar(255),
                           total_cost real,
                           sell_date date NOT NULL,
                           payment_method varchar(255) NOT NULL,
                           status varchar(50) NOT NULL)"""

INSERT_PACKAGE_QUERY = """INSERT INTO diamond_package 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

GET_PACKAGE_ALL_QUERY = """SELECT *
                           FROM diamond_package"""

GET_PACKAGE_QUERY_BY_ID = """SELECT *
                             WHERE package_code=%s"""

DELETE_PACKAGE_ITEM = """DELETE FROM diamond_package
                         WHERE package_code=%s"""
