import json
import os
import time
import random
import datetime

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def generate_sensor_data(data_model):
    timestamp = datetime.datetime.now().isoformat()
    air_temperature = round(random.uniform(10, 30), 2)
    wind_speed = round(random.uniform(0, 15), 2)
    co2_flux = round(random.uniform(-5, 5), 2)
    h2o_flux = round(random.uniform(-2, 2), 2)
    return {
        "timestamp": timestamp,
        "air_temperature": air_temperature,
        "wind_speed": wind_speed,
        "CO2_flux": co2_flux,
        "H2O_flux": h2o_flux
    }

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))

    edge_config_path = os.path.join(base_path, '..', '..', 'edge_config.json')
    sensors_config_path = os.path.join(base_path, '..', '..', 'sensors_config.json')
    data_model_path = os.path.join(base_path, '..', '..', 'data_model.json')
    edge_config = load_config(edge_config_path)
    sensors_config = load_config(sensors_config_path)
    data_model = load_config(data_model_path)

    transfer_interval = edge_config['data_transfer_interval']
    sensor_id = sensors_config['id']

    while True:
        sensor_data = generate_sensor_data(data_model)
        print(f"Sensor ID: {sensor_id}")
        print(f"Data: {sensor_data}")
        time.sleep(transfer_interval)

if __name__ == "__main__":
    main()