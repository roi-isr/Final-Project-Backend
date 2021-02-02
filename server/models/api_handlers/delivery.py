from server.database.queries.delivery import *
from .basic_handler import ApiHandler
from typing import List


class DeliveryHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["delivery_id", "package_code", "delivery_company", "delivery_origin", "seller"]

    def insert(self, delivery_list: List[str]):
        super()._create_table(CREATE_DELIVERY_QUERY)
        super()._insert(INSERT_DELIVERY_QUERY, delivery_list)
        return self._response

    def fetch_all_data(self):
        super()._fetch_all_data(GET_DELIVERY_ALL_QUERY, self.named_values)
        return self._response

    # def fetch_data_by_code(self, package_code: str):
    #     super()._fetch_data(GET_PACKAGE_ALL_QUERY, package_code, self.named_values)
    #     return self._response

    def delete_item(self, delivery_code):
        super()._delete_item(DELETE_DELIVERY_ITEM, delivery_code)
        return self._response
