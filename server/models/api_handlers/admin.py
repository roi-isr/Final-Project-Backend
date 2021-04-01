from server.database.queries.admin import *
from flask import jsonify
from .basic_handler import ApiHandler


class AdminHandler(ApiHandler):
    def __init__(self):
        super().__init__()

    def insert(self, admin_list: list):
        super()._create_table(CREATE_TABLE_QUERY)
        super()._insert(INSERT_ADMIN_QUERY, admin_list)
        return self._response

    def delete(self, _id):
        super()._delete_item(DELETE_ADMIN_ITEM, _id)

    def delete_table(self):
        super()._drop_table(INSERT_ADMIN_QUERY)
        return self._response
