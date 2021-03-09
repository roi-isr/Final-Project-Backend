from server.database.queries.stock import *
from .basic_handler import ApiHandler
from typing import List


class StockHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["stock_id", "package_model", "weight_in_karat",
                             "cost_per_karat", "clearance", "color", "code", "comments",
                             "sell_date", "status"]

    def insert(self, package_list: List[str]):
        super()._create_table(CREATE_STOCK_QUERY)
        super()._insert(INSERT_STOCK_QUERY, package_list)
        return self._response

    def fetch_all_data(self):
        super()._fetch_all_data(GET_STOCK_ALL_QUERY, self.named_values)
        return self._response

    def fetch_data_by_code(self, package_code: str):
        super()._fetch_data(GET_STOCK_ALL_QUERY, package_code, self.named_values)
        return self._response

    def delete_item(self, package_code):
        super()._delete_item(DELETE_STOCK_ITEM, package_code)
        return self._response
