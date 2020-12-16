import psycopg2


class DB:

    def __init__(self):
        self.connction = self.connect_db()
        self.create_table()

    # Create connection between the server and the db
    def connect_db(self):
        connection = psycopg2.connect("""
        dbname='d6sja18bu5d6qh'
        user='srmngikqacnqlj'
        password='c74259d2a98acc497a45815abd47dfd4cf0d29484019b547d1c1b8fe789f9fd2'
        host='ec2-54-170-100-209.eu-west-1.compute.amazonaws.com'
        port='5432'""")
        return connection

    # Create a table, getting its name and fields attributes
    def create_table(self):
        with self.connction as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Contact (email_address varchar(255) NOT NULL, name varchar(255), phone varchar(255),content varchar(555))")

    #insert data for table in the DB
    def insert_data(self, data):
        with self.connction as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Contact VALUES (%s, %s, %s,%s)", (data[0], data[1], data[2], data[3]))

    def get_data(self, email):
        with self.connction as conn:
            cur = conn.cursor()
            cur.execute("SELECT email_address,name,phone,content FROM Contact WHERE email_address=%s; ", (email,))
            return cur.fetchall()