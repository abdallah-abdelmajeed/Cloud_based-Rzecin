from flask import Flask, jsonify, request, abort
import json
from datetime import datetime
import os

app = Flask(__name__)

def load_sensors_config():
    """Loads sensor configurations from sensors_config.json."""
    try:
        with open(os.path.join(os.path.dirname(__file__), '..', '..', 'sensors_config.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: sensors_config.json not found")
        abort(500, "Sensors configuration file not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding sensors_config.json: {e}")
        abort(500, "Error decoding sensors configuration file.")

def load_data():
    """Loads sensor data from sensor_data.json."""
    try:
        data = []
        with open(os.path.join(os.path.dirname(__file__), '..', '..', 'sensor_data.json'), 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: sensor_data.json not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding sensor_data.json: {e}")
        abort(500, "Error decoding sensor data file.")

def filter_data(data, sensor_id, date_range):
    """Filters sensor data by sensor_id and date_range."""
    filtered_data = []
    try:
        start_date_str, end_date_str = date_range.split(',')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    except ValueError:
        abort(400, "Invalid date format. Use YYYY-MM-DD,YYYY-MM-DD")

    for item in data:
        try:
            item_date = datetime.fromisoformat(item['timestamp'])
            if str(item['sensor_id']) == sensor_id and start_date <= item_date <= end_date:
                filtered_data.append(item)
        except (ValueError, KeyError) as e:
            print(f"Skipping item due to formatting issue: {item} - Error: {e}")
            continue

    return filtered_data

@app.route('/sensors', methods=['GET'])
def get_sensors():
    """API endpoint to get all sensors."""
    sensors = load_sensors_config()
    return jsonify(sensors)

@app.route('/data', methods=['GET'])
def get_data():
    """API endpoint to get sensor data filtered by sensor_id and date_range."""
    sensor_id = request.args.get('sensor_id')
    date_range = request.args.get('date_range')

    if not sensor_id or not date_range:
        return "Missing sensor_id or date_range parameter", 400
    
    data = load_data()
    filtered_data = filter_data(data, sensor_id, date_range)    
    return jsonify(filtered_data)


if __name__ == '__main__':
    app.run(debug=False, port=5000)