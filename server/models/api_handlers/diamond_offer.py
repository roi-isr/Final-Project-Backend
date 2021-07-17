from typing import List

from server.database.queries.diamond_offer import *
from .basic_handler import ApiHandler


class OfferHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["offer_id", "package_id", "name",
                             "phone", "email", "offered_weight",
                             "offered_price", "additional_comments", "offer_date"]

    def insert(self, package_list, _id: str):
        super()._create_table(CREATE_OFFER_QUERY)
        # With ID
        package_list_fixed = package_list
        package_list_fixed.insert(0, int(_id))
        super()._insert(INSERT_OFFER_QUERY, package_list_fixed)
        return self._response

    def fetch_all_data(self):
        super()._create_table(CREATE_OFFER_QUERY)
        super()._fetch_all_data(GET_SPECIFIC_OFFER_QUERY, self.named_values)
        return self._response

    def delete_item(self, package_id: str):
        super()._delete_item(DELETE_OFFER_ITEM, package_id)
        return self._response
