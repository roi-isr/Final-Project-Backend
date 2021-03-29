from server.database.queries.stock import *
from .basic_handler import ApiHandler
from typing import List
from flask import jsonify
from server.database.database import Database


class StockHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["stock_id", "package_model", "weight_in_karat",
                             "cost_per_karat", "clearance", "color", "code", "comments",
                             "sell_date", "status"]
        self.offer_named_values = ["offer_id", "stock_id", "package_model", "code", "name", "phone", "email",
                                   "offered_weight", "offered_price", "additional_comments"]

    def insert(self, package_list: List[str]):
        super()._create_table(CREATE_STOCK_QUERY)
        super()._insert(INSERT_STOCK_QUERY, package_list)
        return self._response

    def fetch_all_data(self):
        super()._create_table(CREATE_STOCK_QUERY)
        super()._fetch_all_data(GET_STOCK_ALL_QUERY, self.named_values)
        return self._response

    def fetch_data_by_code(self, package_code: str):
        super()._create_table(CREATE_STOCK_QUERY)
        super()._fetch_data(GET_STOCK_ALL_QUERY, package_code, self.named_values)
        return self._response

    def update_item(self, package_id: str, new_package_list: List[str]):
        # Exclude IDs
        keys_str = ', '.join(self.named_values[1:-1])
        fixed_query = UPDATE_STOCK_ITEM_QUERY.format(keys_str)
        super()._update_item(fixed_query, package_id, new_package_list)
        return self._response

    def update_item_status(self, package_id: str, wanted_status: str):
        # status validation
        if not (wanted_status == 'בחנות' or wanted_status == 'לא בחנות'):
            self._response = self._build_response(data=jsonify({"message": "Invalid body content"}),
                                                  status_code=400)
        else:
            super()._update_item(UPDATE_STOCK_STATUS_QUERY, package_id, wanted_status)
        return self._response

    def delete_item(self, package_id: str):
        self.__delete_related_offers(package_id)
        super()._delete_item(DELETE_STOCK_ITEM, package_id)
        return self._response

    def __delete_related_offers(self, package_id: str):
        super()._delete_item(DELETE_RELATED_OFFERS_QUERY, package_id)

    def get_stocks_to_offers_counter(self):
        database = Database()
        data = database.fetch_all_data(STOCK_TO_OFFER_ALL_QUERY)
        self.__handle_stock_to_offer_dict(data)
        return self._response

    # Transfer the result into a dictionary
    def __handle_stock_to_offer_dict(self, data):
        if data:
            data_dict = {data[i][0]: data[i][1]
                         for i in range(len(data))}
            self._response = self._build_response(data=jsonify(data_dict),
                                                  status_code=200)
        else:
            self._response = self._build_response(data=jsonify({'message': 'Item doesn\'t found'}),
                                                  status_code=404)

    def get_stock_to_offers(self, stock_id):
        super()._fetch_data(STOCK_TO_OFFER_ONE_QUERY, stock_id, self.offer_named_values)
        return self._response
