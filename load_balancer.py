from flask import Flask, request, jsonify, send_from_directory
import requests
import time
import threading

app = Flask(__name__)

active_instances = []  # Список активных инстансов
inactive_instances = []  # Список недоступных инстансов
current_index = 0  # Индекс для стратегии Round Robin

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"instances": active_instances})

@app.route('/process', methods=['GET'])
def process():
    global current_index
    if not active_instances:
        return jsonify({"error": "No available instances"}), 503

    # Стратегия Round Robin
    instance = active_instances[current_index]
    current_index = (current_index + 1) % len(active_instances)
    try:
        response = requests.get(f"http://{instance}/process")
        return jsonify(response.json())
    except requests.exceptions.RequestException:
        return jsonify({"error": "Failed to connect to instance"}), 503

@app.route('/add_instance', methods=['POST'])
def add_instance():
    data = request.json
    instance = f"{data['ip']}:{data['port']}"
    if instance not in active_instances and instance not in inactive_instances:
        active_instances.append(instance)
    return jsonify({"message": "Instance added", "instances": active_instances})

@app.route('/remove_instance', methods=['POST'])
def remove_instance():
    index = request.json['index']
    if 0 <= index < len(active_instances):
        active_instances.pop(index)
        return jsonify({"message": "Instance removed", "instances": active_instances})
    return jsonify({"error": "Invalid index"}), 400

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

def check_health():
    while True:
        # Проверяем активные инстансы
        for instance in active_instances[:]:
            try:
                response = requests.get(f"http://{instance}/health")
                if response.status_code != 200:
                    active_instances.remove(instance)
                    inactive_instances.append(instance)
            except requests.exceptions.RequestException:
                active_instances.remove(instance)
                inactive_instances.append(instance)

        # Проверяем недоступные инстансы
        for instance in inactive_instances[:]:
            try:
                response = requests.get(f"http://{instance}/health")
                if response.status_code == 200:
                    inactive_instances.remove(instance)
                    active_instances.append(instance)
            except requests.exceptions.RequestException:
                pass

        time.sleep(5)

if __name__ == '__main__':
    threading.Thread(target=check_health, daemon=True).start()
    app.run(port=5000)
