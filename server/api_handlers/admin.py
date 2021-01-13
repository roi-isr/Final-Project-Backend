from ..database.admin import AdminDatabase
from flask import jsonify
from .build_response.build_response import build_response


def verified():
    return jsonify({"auth": "Authenticated User"})
    json_info = jsonify({"auth": "Authenticated User"})
    return build_response(data=json_info, status_code=200)


def add(admin_list):
    database = AdminDatabase()
    # If table doesn't exists
    database.create_table()
    extracted_list = list(admin_list.values())
    database.add_admin(extracted_list)
    database.close_connection()
    json_info = jsonify({"message": "Successful POST request"})
    return build_response(data=json_info, status_code=201)


# def delete(admin_id):
#     database = AdminDatabase()
#

def delete_table():
    database = AdminDatabase()
    database.drop_table()
    database.close_connection()
    json_info = jsonify({"message": "Successful DELETE request"})
    return build_response(data=json_info, status_code=200)
