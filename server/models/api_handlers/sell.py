from server.database.queries.sell import *
from .basic_handler import ApiHandler
from typing import List


class SellHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["sell_id", "package_code", "package_model",
                             "weight_in_carat", "price_per_carat", "buying_entity",
                             "sell_date", "payment_method"]

    def insert(self, package_list: List[str]):
        super()._create_table(CREATE_SELL_QUERY)
        super()._insert(INSERT_SELL_QUERY, package_list)
        return self._response

    def fetch_all_data(self):
        super()._create_table(CREATE_SELL_QUERY)
        super()._fetch_all_data(GET_SELL_ALL_QUERY, self.named_values)
        return self._response

    def update_item(self, package_id: str, new_package_list: List[str]):
        # Exclude IDs
        keys_str = ', '.join(self.named_values[1:])
        fixed_query = UPDATE_SELL_ITEM_QUERY.format(keys_str)
        super()._update_item(fixed_query, package_id, new_package_list)
        return self._response

    def delete_item(self, package_id: str):
        super()._delete_item(DELETE_SELL_ITEM, package_id)
        return self._response
