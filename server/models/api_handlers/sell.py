from server.database.queries.sell import *
from server.database.queries.stock import *
from server.database.queries.ML_sells import *
from server.database.queries.admin_price_advice import *
from server.database.database import *
from .basic_handler import ApiHandler
from typing import List
from server.ML.ML_main import build_ml_sells_models

class SellHandler(ApiHandler):
    def __init__(self):
        super().__init__()
        self.named_values = ["sell_id", "package_code", "package_model",
                             "weight_in_carat", "price_per_carat", "buying_customer",
                             "sell_date", "payment_method"]

        self.customer_named_values = ["buying_customer", "customer_phone", "customer_mail"]

    @staticmethod
    def __update_stock(package_list, prev_weight=None):
        db = Database()
        code = package_list[0]
        weight_to_reduce = float(package_list[2]) if prev_weight is None else float(package_list[2]) - prev_weight
        try:
            stock_balance = float(db.fetch_specific_data(SELECT_STORE_STOCK, (code,))[0][0])
            weight_diff = stock_balance - weight_to_reduce
        except IndexError:
            stock_balance = None
        if stock_balance is not None:
            if weight_diff > 0:
                print(weight_to_reduce)
                db.update_item(UPDATE_STORE_STOCK, weight_to_reduce, code)
            else:
                stock_id = db.fetch_specific_data(GET_STOCK_ID_QUERY, (code,))[0][0]
                db.delete_item(DELETE_RELATED_OFFERS_QUERY, (stock_id,))
                db.delete_item(DELETE_STOCK_ITEM, (stock_id,))

    def insert(self, package_list: List[str]):
        super()._create_table(CREATE_SELL_QUERY)
        super()._insert(INSERT_SELL_QUERY, package_list)
        self.__update_stock(package_list)
        return self._response

    def fetch_all_data(self):
        super()._create_table(CREATE_SELL_QUERY)
        super()._fetch_all_data(GET_SELL_ALL_QUERY, self.named_values)
        return self._response

    def update_item(self, package_id: str, new_package_list: List[str]):
        # Exclude IDs
        db = Database()
        code = package_id
        prev_weight = float(db.fetch_specific_data(GET_PREV_WEIGHT_QUERY, (code,))[0][0])
        keys_str = ', '.join(self.named_values[1:])
        fixed_query = UPDATE_SELL_ITEM_QUERY.format(keys_str)
        super()._update_item(fixed_query, package_id, new_package_list)
        print(f'prev: {prev_weight}')
        self.__update_stock(new_package_list, prev_weight)
        return self._response

    def delete_item(self, sell_id: str):
        super()._delete_item(DELETE_SELL_ITEM, sell_id)
        return self._response

    def fetch_customer(self, sell_id: str):
        super()._create_table(CREATE_SELL_QUERY)
        super()._fetch_data(GET_CUSTOMER_QUERY, sell_id, self.customer_named_values)
        return self._response

    def insert_sell_ml(self, sell_list: List[str]):
        super()._create_table(CREATE_SELL_DATA_QUERY)
        super()._insert(INSERT_SELL_DATA_QUERY, sell_list)
        try:
            build_ml_sells_models()
        except:
            pass
        return self._response

    # Reset models from DB
    def reset_models(self):
        super()._drop_table(RESET_ADVISE_MODEL_QUERY)
        super()._drop_table(RESET_SELLS_MODEL_QUERY)
        return self._response
