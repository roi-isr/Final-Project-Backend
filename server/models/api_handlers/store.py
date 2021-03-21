from server.database.queries.store import *
from .basic_handler import ApiHandler
from typing import List


class StoreHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["stock_id", "package_model", "weight_in_karat",
                             "cost_per_karat", "clearance", "color"]

    def fetch_all_data(self):
        super()._fetch_all_data(GET_STORE_ALL_QUERY, self.named_values)
        return self._response
