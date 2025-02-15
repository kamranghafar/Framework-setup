import os
import subprocess
from datetime import datetime
import http.server
import socketserver
import threading
import webbrowser
import time
import random
import string

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

random_id = generate_random_string(3)

def run_tests_and_generate_report():
    # Create a unique folder with today's date
    today = datetime.now().strftime("%Y-%m-%d")
    results_dir = f"allure_results_{today}_{random_id}"
    report_dir = f"TestReport_{today}_{random_id}/allure_report"

    # Create directories if they don't exist
    os.makedirs(results_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)

    # Define commands
    behave_command = ["behave", "--tags=@smoke", "-f", "allure_behave.formatter:AllureFormatter", "-o", results_dir]
    allure_generate_command = ["allure", "generate", results_dir, "-o", report_dir, "--clean"]

    try:
        # Run behave command to generate allure results
        subprocess.run(behave_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Behave command failed with exit code {e.returncode}")

    # Generate the allure report
    subprocess.run(allure_generate_command, shell=True, check=True)

    # Serve the generated report
    serve_report(report_dir)

def serve_report(report_dir):
    # Define the handler to serve files from the report directory
    handler = http.server.SimpleHTTPRequestHandler
    os.chdir(report_dir)

    # Define the server
    PORT = 8000
    httpd = socketserver.TCPServer(("", PORT), handler)

    # Open the report in the default web browser
    webbrowser.open(f"http://localhost:{PORT}/index.html")

    # Start the server
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.start()

    # Allow some time for the browser to load the report
    time.sleep(20)

    # Shutdown the server
    httpd.shutdown()
    server_thread.join()

if __name__ == "__main__":
    run_tests_and_generate_report()
