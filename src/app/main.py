import multiprocessing
import os
import time
from src.app.api import app  
from src.cloud.data_handler import handle_data


def run_api():
    app.run(debug=True, use_reloader=False)


def run_data_handler():
    handle_data()


def get_pid():
    print(f"Current PID: {os.getpid()}")


if __name__ == "__main__":
    get_pid()

    data_handler_process = multiprocessing.Process(target=run_data_handler, daemon=True)
    data_handler_process.start()

    run_api()

    data_handler_process.join()

