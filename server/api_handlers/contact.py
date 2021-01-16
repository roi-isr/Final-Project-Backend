from ..database.contact import ContactDatabase
from flask import jsonify
from .build_response.build_response import build_response


def get_info(email):
    database = ContactDatabase()
    data = database.get_data(email)
    data_dict = {i: data[i] for i in range(len(data))}
    database.close_connection()
    json_info = jsonify(data_dict)
    return build_response(data=json_info, status_code=200)


def insert(contact_info):
    database = ContactDatabase()
    database.create_table()
    extracted_list = list(contact_info.values())
    database.insert_data(extracted_list)
    database.close_connection()
    json_info = jsonify({"message": "Successful POST"})
    return build_response(data=json_info, status_code=201)
