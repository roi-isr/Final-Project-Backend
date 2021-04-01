from server.database.queries.admin_price_advice import *
from .basic_handler import ApiHandler
from typing import List
from server.ML.ML_main import build_ml_advise_models


class AdminAdviseHandler(ApiHandler):
    def __init__(self):
        super().__init__()

    def insert(self, advise_list: List[str]):
        super()._create_table(CREATE_ADVICE_TABLE_QUERY)
        super()._insert(INSERT_ADVISE_QUERY, advise_list)
        # Build ML model over admin advise
        try:
            build_ml_advise_models()
        except:
            pass
        return self._response


