import hashlib

<<<<<<< HEAD
=======
from flask import jsonify

>>>>>>> e83dbabce7c0587ef257f2c4a83420d405a985d1
from server.database.queries.admin import *
from .basic_handler import ApiHandler


class AdminHandler(ApiHandler):
    def __init__(self):
        super().__init__()

    # hash the password
    @staticmethod
    def _hash_pwd(password: str):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed_password

    def insert(self, admin_list: list):
        username = admin_list[0]
        secured_password = self._hash_pwd(admin_list[1])

        super()._create_table(CREATE_TABLE_QUERY)
        super()._insert(INSERT_ADMIN_QUERY, [username, secured_password])
        return self._response

    def delete(self, _id):
        super()._delete_item(DELETE_ADMIN_ITEM, _id)

    def delete_table(self):
        super()._drop_table(INSERT_ADMIN_QUERY)
        return self._response
