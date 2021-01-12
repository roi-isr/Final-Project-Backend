from ..database.contact import ContactDatabase
from flask import jsonify


def get_info(email):
    database = ContactDatabase()
    data = database.get_data(email)
    data_dict = {i: data[i] for i in range(len(data))}
    database.close_connection()
    return jsonify(data_dict)


def insert(contact_info):
    database = ContactDatabase()
    database.create_table()
    database.insert_data(list(contact_info.values()))
    database.close_connection()
    return jsonify({"message": "Successful POST"})
