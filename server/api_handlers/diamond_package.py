from server.database.queries.diamond_package import *
from .handler import ApiHandler
from typing import List


class PackageHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["package_code", "weight_in_karat", "cost_per_karat", "clearance", "color", "seller",
                             "total_cost", "sell_date", "payment_method", "status"]

    def insert(self, package_list: List[str]):
        super()._create_table(CREATE_PACKAGE_QUERY)
        super()._insert(INSERT_PACKAGE_QUERY, package_list)
        return self._response

    def fetch_all_data(self):
        super()._fetch_all_data(GET_PACKAGE_ALL_QUERY, self.named_values)
        return self._response

    def fetch_data_by_code(self, package_code: str):
        super()._fetch_data(GET_PACKAGE_ALL_QUERY, package_code, self.named_values)
        return self._response

    def delete_item(self, package_code):
        super()._delete_item(DELETE_PACKAGE_ITEM, package_code)
        return self._response
