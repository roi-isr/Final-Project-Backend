from server.database.queries.contact import *
from typing import List
from .basic_handler import ApiHandler


class ContactHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["email", "name", "phone", "content", "create_at"]

    def get_info(self, email: str):
        super()._fetch_data(GET_DATA_QUERY, email, self.named_values)
        return self._response

    def get_info_all(self):
        super()._fetch_all_data(GET_DATA_ALL_QUERY, self.named_values)
        return self._response

    def insert(self, contact_info: List[str]):
        super()._create_table(CREATE_TABLE_QUERY)
        super()._insert(INSERT_DATA_QUERY, contact_info)
