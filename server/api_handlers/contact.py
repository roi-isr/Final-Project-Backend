from server.database.queries.contact import *
from flask import jsonify
from .build_response.build_response import build_response
from .handler import ApiHandler


class ContactHandler(ApiHandler):
    def __init__(self):
        super().__init__()

    def get_info(self, email):
        super()._fetch_data(GET_DATA_QUERY, (email,))
        return self._response

    def insert(self, contact_info):
        super()._create_table(CREATE_TABLE_QUERY)
        super()._insert(INSERT_DATA_QUERY, contact_info)
