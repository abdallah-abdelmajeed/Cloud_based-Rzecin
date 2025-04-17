import json
import os


def load_config(config_file):
    """Loads configuration from a JSON file.

    Args:
        config_file (str): The path to the configuration file.

    Returns:
        dict: The configuration data as a dictionary, or None if there was an error.
    """
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{config_file}': {e}")
    
def handle_data():
    """
    Handles data received from the edge device.
    Reads data from the console, parses it, and stores it in a local file.
    """
    data_file = "sensor_data.txt"  # File to store received data
    # Create the file if it does not exists
    if not os.path.exists(data_file):
        with open(data_file, 'w') as f:
          json.dump([],f)
    
    while True:
        try:
            line = input()
            try:
                data = json.loads(line)

                with open(data_file, "r+") as f:
                  try:
                    file_data = json.load(f)
                  except json.JSONDecodeError:
                    file_data=[]
                  file_data.append(data)
                  f.seek(0)
                  json.dump(file_data,f,indent=4)
                  print(f"Data received and stored in {data_file}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON line: {line}. Error: {e}")

        except EOFError:
            print("End of input reached, stopping data handler")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
    