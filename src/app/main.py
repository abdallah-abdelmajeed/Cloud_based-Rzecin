import multiprocessing
import os
import time
from src.app.api import app as api_app
from src.app.dashboard import app as dashboard_app, start_dashboard
from src.cloud.data_handler import handle_data


def run_api():
    api_app.run(debug=True, use_reloader=False, port=5000)


def run_data_handler():
    handle_data()


def get_pid():
    print(f"Current PID: {os.getpid()}")


def run_dashboard():
    start_dashboard()

if __name__ == "__main__":
    get_pid()

    # Start data handler process
    data_handler_process = multiprocessing.Process(target=run_data_handler, daemon=True)
    data_handler_process.start()
    
    # Start dashboard process
    dashboard_process = multiprocessing.Process(target=run_dashboard, daemon=True)
    dashboard_process.start()
    
    # Run API in main process
    run_api()
    
    # Join processes
    data_handler_process.join()
    dashboard_process.join()

