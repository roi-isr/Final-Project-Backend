from ..database.admin import AdminDatabase
from flask import jsonify


def verified():
    return jsonify({"auth": "Authenticated User"})


def add(admin_list):
    database = AdminDatabase()
    database.create_table()
    database.add_admin(list(admin_list.values()))
    database.close_connection()
    return jsonify({"message": "Successful POST request"})


def delete_table():
    database = AdminDatabase()
    database.drop_table()
    database.close_connection()
    return jsonify({"message": "Successful DELETE request"})
