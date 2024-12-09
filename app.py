import json
from flask import Flask, request, jsonify, send_from_directory
from flask_limiter import Limiter

# Инициализация приложения Flask и лимитера
app = Flask(__name__)
limiter = Limiter(app)

# Хранилище данных
data = {}

# Загрузка данных из файла
def load_data():
    global data
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

# Сохранение данных в файл
def save_data():
    with open('data.json', 'w') as f:
        json.dump(data, f)

# Загрузка данных при старте приложения
load_data()

# Маршрут для корневого URL, возвращает HTML-страницу
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Установка общего лимита на 100 запросов в сутки
@limiter.limit("100 per day")
@app.route('/set', methods=['POST'])
def set_value():
    key = request.json.get('key')
    value = request.json.get('value')
    data[key] = value
    save_data()
    return jsonify({"message": "Key-Value pair saved."}), 201

@limiter.limit("100 per day")
@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    value = data.get(key)
    if value is not None:
        return jsonify({"value": value}), 200
    return jsonify({"error": "Key not found."}), 404

@limiter.limit("10 per minute")
@app.route('/delete/<key>', methods=['DELETE'])
def delete_key(key):
    if key in data:
        del data[key]
        save_data()
        return jsonify({"message": "Key deleted."}), 200
    return jsonify({"error": "Key not found."}), 404

@limiter.limit("100 per day")
@app.route('/exists/<key>', methods=['GET'])
def exists(key):
    exists = key in data
    return jsonify({"exists": exists}), 200

if __name__ == '__main__':
    app.run(debug=True)
