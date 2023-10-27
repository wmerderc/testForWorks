from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Подключение к MongoDB
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["mydatabase"]
collection = db["mycollection"]

# Метод для создания значения
@app.route('/create', methods=['POST'])
def create():
    data = request.json
    if data:
        result = collection.insert_one(data)
        return jsonify({"message": "Значение создано успешно", "id": str(result.inserted_id)}), 201
    return jsonify({"error": "Предоставленные неверные данные"}), 400

# Метод для обновления значения
@app.route('/update/<id>', methods=['PUT'])
def update(id):
    data = request.json
    if data:
        result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.modified_count > 0:
            return jsonify({"message": "Значение успешно обновлено"}), 200
    return jsonify({"error": "Значение не найдено или предоставлены неверные данные"}), 404

# Метод для чтения значения
@app.route('/read/<id>', methods=['GET'])
def read(id):
    value = collection.find_one({"_id": ObjectId(id)})
    if value:
        return jsonify({"value": value}), 200
    return jsonify({"error": "Значение не найдено"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
