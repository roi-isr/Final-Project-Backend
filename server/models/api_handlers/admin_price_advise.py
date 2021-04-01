from server.database.queries.admin_price_advice import *
from .basic_handler import ApiHandler
from typing import List


class AdminAdviseHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["advise_id", "weight", "cut", "clarity",
                             "color", "table", "depth"]

    def insert(self, advise_list: List[str]):
        super()._create_table(CREATE_TABLE_QUERY)

        super()._insert(INSERT_ADVISE_QUERY, advise_list)
        return self._response

    def fetch_all_data(self):
        super()._create_table(CREATE_TABLE_QUERY)
        super()._fetch_all_data(GET_ADVISE_ALL_QUERY, self.named_values)
        return self._response

