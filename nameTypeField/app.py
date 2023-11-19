from flask import Flask, request, jsonify
from pymongo import MongoClient
import re

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")

db = client["nameTypeFields"]
collection = db["nameTypeFileds"]

def is_phone(value):
    """
    Проверяет, является ли строка валидным номером телефона.
    """
    pattern = re.compile(r'^\+7\d{3}\d{3}\d{2}\d{2}$')
    return bool(pattern.match(value))

def is_email(value):
    """
    Проверяет, является ли строка валидным адресом электронной почты.
    """
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(value))

def is_date(value):
    """
    Проверяет, соответствует ли строка форматам DD.MM.YYYY или YYYY-MM-DD.
    """
    pattern_dd_mm_yyyy = re.compile(r'^\d{2}\.\d{2}.\d{4}$')
    pattern_yyyy_mm_dd = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(pattern_dd_mm_yyyy.match(value)) or bool(pattern_yyyy_mm_dd.match(value))

def get_template_name(form_data):
    """
    Определяет имя шаблона по данным формы.
    """
    keys = ['field0', 'field1', 'field2', 'field3']
    known_keys_values = {}

    for key, value in form_data.items():
        if key == "email" and is_email(value):
            known_keys_values['field0'] = key
        elif key == "phone" and is_phone(value):
            known_keys_values['field1'] = key
        elif key == "date" and is_date(value):
            known_keys_values['field2'] = key
        elif key == "text":
            known_keys_values['field3'] = key
        else:
            return None

    query = {
        '$and': [
            {key: {'$exists': False} for key in keys if key not in known_keys_values},
            {key: value for key, value in known_keys_values.items()},
            {'name': {'$exists': True}},
        ]
    }

    template = collection.find_one(query)
    if template:
        return template.get("name")
    else:
        return None

@app.route("/get_form", methods=["POST"])
def get_form():
    """
    Обработчик запроса на получение формы.
    """
    form_data = {}
    for key, value in request.args.items():
        form_data[key] = value

    template_name = get_template_name(form_data)
    if template_name:
        return jsonify({"template_name": template_name})
    else:
        field_type = []
        for key, value in form_data.items():
            if is_date(value):
                field_type.append("DATE")
            elif is_email(value):
                field_type.append("EMAIL")
            elif is_phone(value):
                field_type.append("PHONE")
            else:
                field_type.append("TEXT")

        result = {field: field_type for field, field_type in zip(form_data, field_type)}
        return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
