""" Defining a DB class, which implements a direct connection and action functions with the PostgreSQL DB"""

from typing import List, Tuple
import psycopg2
from server.config.connection_config import CONNECTION_INFO


class Database:
    def __init__(self):
        self.connection = self.__connect()

    @staticmethod
    # Create connection between the server and db
    def __connect():
        connection = psycopg2.connect(CONNECTION_INFO)
        return connection

    # Create a table, getting its name and fields attributes
    def create_table(self, query: str):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query)

    # Insert data for table in the DB
    def insert_data(self, query: str, data: Tuple[str]):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query, data)

    # Retrieve data from DB
    def fetch_all_data(self, query: str) -> List[str]:
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query)
            return cur.fetchall()

    # Retrieve data from DB
    def fetch_specific_data(self, query: str, data: Tuple[str]) -> List[str]:
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query, data)
            return cur.fetchall()

    def delete_item(self, query: str, item_id: Tuple[str]) -> List[str]:
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query, item_id)
            return cur.fetchall()

    def drop_table(self, query: str):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(query)

    # Close open connection with DB
    def close_connection(self):
        self.connection.close()
