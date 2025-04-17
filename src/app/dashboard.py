from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import json
import os
import threading
import time
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rzecin-dashboard-secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Path to the sensor data file
SENSOR_DATA_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'sensor_data.txt')

# Create templates directory if it doesn't exist
templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
os.makedirs(templates_dir, exist_ok=True)

# Create static directory for CSS and JS files
static_dir = os.path.join(os.path.dirname(__file__), 'static')
os.makedirs(static_dir, exist_ok=True)
os.makedirs(os.path.join(static_dir, 'js'), exist_ok=True)
os.makedirs(os.path.join(static_dir, 'css'), exist_ok=True)

def load_sensor_data():
    """Load the latest sensor data from the file"""
    try:
        if os.path.exists(SENSOR_DATA_FILE):
            with open(SENSOR_DATA_FILE, 'r') as f:
                try:
                    data = json.load(f)
                    # Return the last 50 data points or all if less than 50
                    return data[-50:] if len(data) > 50 else data
                except json.JSONDecodeError:
                    return []
        return []
    except Exception as e:
        print(f"Error loading sensor data: {e}")
        return []

def background_thread():
    """Background thread that emits sensor data to connected clients"""
    last_data_length = 0
    
    while True:
        # Check for new data
        current_data = load_sensor_data()
        current_length = len(current_data)
        
        if current_length > last_data_length:
            # New data available
            new_data = current_data[last_data_length:]
            for data_point in new_data:
                socketio.emit('sensor_update', data_point)
            
            # Also emit the full dataset for chart initialization/updates
            socketio.emit('sensor_history', current_data)
            
            last_data_length = current_length
        
        # Sleep to avoid excessive CPU usage
        time.sleep(5)

@app.route('/')
def index():
    """Render the dashboard homepage"""
    return render_template('dashboard.html')

@app.route('/api/sensor-data')
def get_sensor_data():
    """API endpoint to get the latest sensor data"""
    data = load_sensor_data()
    return jsonify(data)

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    print('Client connected')
    # Send initial data to the client
    socketio.emit('sensor_history', load_sensor_data())

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    print('Client disconnected')

def start_dashboard():
    """Start the dashboard server"""
    # Start the background thread for data updates
    thread = threading.Thread(target=background_thread)
    thread.daemon = True
    thread.start()
    
    # Start the Flask-SocketIO server
    socketio.run(app, debug=True, host='0.0.0.0', port=5001, use_reloader=False)

if __name__ == '__main__':
    start_dashboard()