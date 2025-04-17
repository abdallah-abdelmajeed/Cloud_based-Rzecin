#!/bin/bash

# Start data_handler.py in the background
python3 src/cloud/data_handler.py &
data_handler_pid=$!
echo "Data handler started with PID: $data_handler_pid"

# Start edge_simulator.py in the background
python3 src/edge/edge_simulator.py &
edge_simulator_pid=$!
echo "Edge simulator started with PID: $edge_simulator_pid"

# Wait for 5 seconds
sleep 5
echo "Wait finished, starting main.py"

# Start main.py
python3 src/app/main.py

echo "All processes started"

# Keep the script running until the user exits
wait $data_handler_pid $edge_simulator_pid