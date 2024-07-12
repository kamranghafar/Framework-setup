import subprocess
import os
import sys
import urllib.request
import zipfile
import shutil

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.returncode != 0:
            print(f"Error executing command: {command}\n{result.stderr}")
        else:
            print(f"Executed command: {command}\n{result.stdout}")
    except Exception as e:
        print(f"Exception executing command: {command}\n{str(e)}")

def install_python():
    print("Python installation skipped. Please ensure Python is installed.")

def install_pycharm():
    print("Please download and install PyCharm from https://www.jetbrains.com/pycharm/download/")

def install_dependencies():
    dependencies = ["selenium", "webdriver_manager", "allure-behave", "requests"]
    for package in dependencies:
        print(f"Installing {package}...")
        run_command(f"pip install {package}")

def setup_allure():
    try:
        allure_url = "https://github.com/allure-framework/allure2/releases/download/2.13.9/allure-2.13.9.zip"
        allure_zip = "allure.zip"
        allure_dir = "allure"

        if os.path.exists(allure_dir):
            print("Allure already exists. Skipping download.")
        else:
            print("Downloading Allure...")
            urllib.request.urlretrieve(allure_url, allure_zip)
            print("Extracting Allure...")
            with zipfile.ZipFile(allure_zip, 'r') as zip_ref:
                zip_ref.extractall(allure_dir)

            program_files = os.environ.get("ProgramFiles", "C:\\Program Files")
            allure_path = os.path.join(program_files, "allure")
            if os.path.exists(allure_path):
                shutil.rmtree(allure_path)
            shutil.move(allure_dir, allure_path)
            os.environ["PATH"] += os.pathsep + os.path.join(allure_path, "bin")
            print("Allure installed and PATH updated.")

        # Create run-testcases.py script
        create_run_testcases_script()
    except Exception as e:
        print(f"Error setting up Allure: {str(e)}")

def install_java():
    try:
        java_home = "C:\\Program Files\\Java\\jdk-17"
        if os.path.exists(java_home):
            print("Java is already installed.")
        else:
            java_url = "https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe"
            java_installer = "jdk_installer.exe"
            print("Downloading Java...")
            urllib.request.urlretrieve(java_url, java_installer)
            print("Running Java installer...")
            run_command(java_installer)
            os.environ["JAVA_HOME"] = java_home
            os.environ["PATH"] += os.pathsep + os.path.join(java_home, "bin")
            print("Java installed and JAVA_HOME set.")
    except Exception as e:
        print(f"Error installing Java: {str(e)}")

def create_elements_folder():
    try:
        elements_folder = "elements"
        if not os.path.exists(elements_folder):
            os.makedirs(elements_folder)
            print(f"Created folder: {elements_folder}")

        sample_file_path = os.path.join(elements_folder, "sample_element.py")
        if not os.path.exists(sample_file_path):
            with open(sample_file_path, 'w') as file:
                file.write("# Add page elements here\n")
            print(f"Created sample file: {sample_file_path}")
        else:
            print(f"Sample file {sample_file_path} already exists.")
    except Exception as e:
        print(f"Error creating elements folder: {str(e)}")

def create_features_folder():
    try:
        features_folder = "features"
        steps_folder = os.path.join(features_folder, "steps")

        if not os.path.exists(features_folder):
            os.makedirs(features_folder)
            print(f"Created folder: {features_folder}")
        if not os.path.exists(steps_folder):
            os.makedirs(steps_folder)
            print(f"Created folder: {steps_folder}")

        feature_file_path = os.path.join(features_folder, "search_google.feature")
        if not os.path.exists(feature_file_path):
            with open(feature_file_path, 'w') as file:
                file.write("""Feature: Search Google

@smoke
Scenario: Search for "kamran ghaffar" on Google and click the first link
    Given the user is on the Google homepage
    When the user searches for "kamran ghaffar"
    Then the user clicks on the first search result
""")
            print(f"Created feature file: {feature_file_path}")
        else:
            print(f"Feature file {feature_file_path} already exists.")

        steps_file_path = os.path.join(steps_folder, "search_google_steps.py")
        if not os.path.exists(steps_file_path):
            with open(steps_file_path, 'w') as file:
                file.write("""from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('the user is on the Google homepage')
def step_given_user_on_google_homepage(context):
    context.driver.get("https://www.google.com")

@when('the user searches for "kamran ghaffar"')
def step_when_user_searches(context):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys("kamran ghaffar" + Keys.RETURN)

@then('the user clicks on the first search result')
def step_then_click_first_result(context):
    first_result = context.driver.find_element(By.CSS_SELECTOR, 'h3')
    first_result.click()
""")
            print(f"Created steps file: {steps_file_path}")
        else:
            print(f"Steps file {steps_file_path} already exists.")

        environment_file_path = os.path.join(features_folder, "environment.py")
        if not os.path.exists(environment_file_path):
            with open(environment_file_path, 'w') as file:
                file.write("""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from configuration import configuration_system
from methods.utilities import *

def before_all(context):
    # Executed once before any scenarios are run
    pass

def before_feature(context, feature):
    # Executed before each feature is run
    pass

def before_scenario(context, scenario):
    # for Headless mode
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")

    # Initialize the Chrome service
    service = Service(ChromeDriverManager().install())

    # Initialize the WebDriver with options and service
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set window size and implicit wait time
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)

def after_scenario(context, scenario):
    # Close the browser after each scenario
    context.driver.quit()

def after_step(context, step):
    if configuration_system.screenshot:
        step_capture_screenshot(context)

def after_feature(context, feature):
    # Executed after each feature is run
    pass

def after_all(context):
    # Executed once after all scenarios are run
    passed_scenarios = [scenario for scenario in context._runner.features if scenario.status.name == "passed"]
    failed_scenarios = [scenario for scenario in context._runner.features if scenario.status.name == "failed"]
    if configuration_system.report:
        send_teams_webhook(passed_scenarios, failed_scenarios)
""")
            print(f"Created environment file: {environment_file_path}")
        else:
            print(f"Environment file {environment_file_path} already exists.")
    except Exception as e:
        print(f"Error creating features folder: {str(e)}")

def create_methods_folder():
    try:
        methods_folder = "methods"
        if not os.path.exists(methods_folder):
            os.makedirs(methods_folder)
            print(f"Created folder: {methods_folder}")

        utilities_file_path = os.path.join(methods_folder, "utilities.py")
        if not os.path.exists(utilities_file_path):
            with open(utilities_file_path, 'w') as file:
                file.write("""import random
import os
import allure
import requests
from selenium.common.exceptions import NoSuchElementException
import configuration

def step_capture_screenshot(context):
    # Capture screenshot and save it in the "screenshots" directory
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    random_3_digit_number = random.randint(100, 999)
    ran_num = str(random_3_digit_number)
    screenshot_name = "screenshot" + ran_num + ".png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)
    context.driver.save_screenshot(screenshot_path)
    # Attach the screenshot to the Allure report
    with allure.step('Attach Screenshot'):
        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG, name=screenshot_name)

def trigger_webhook(total_failures, failure_details):
    # Use the correct webhook URL from configuration
    teams_webhook_url = configuration.configuration_system.webhook_url
    payload = {
        "@type": "MessageCard",
        "@context": "",
        "summary": "Test Automation Failure",
        "title": "Failed Failed Failed!!!!",
        "sections": [{
            "activityTitle": "Test Automation Failure Details",
            "activitySubtitle": f"Total Failures: {total_failures}",
            "facts": [{
                "name": "Total Failures",
                "value": total_failures
            }] + [
                         {
                             "name": f"Failure {i + 1}",
                             "value": detail
                         } for i, detail in enumerate(failure_details)
                     ]
        }]
    }
    try:
        response = requests.post(teams_webhook_url, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
    except Exception as e:
        print("Error triggering webhook:", e)

def assert_element_exists(driver, by, locator, failure_details):
    try:
        driver.find_element(by, locator)
    except NoSuchElementException:
        failure_details.append(f"Element not found: {locator}")
        total_failures = len(failure_details)
        trigger_webhook(total_failures, failure_details)
        raise AssertionError(f"Element not found: {locator}")

def send_teams_webhook(passed_scenarios, failed_scenarios):
    # Teams webhook URL
    webhook_url = configuration.configuration_system.webhook_url

    # Format message for Teams
    message = f"Total passed Features: {len(passed_scenarios)}\n"
    message += f"Total failed Features: {len(failed_scenarios)}\n"
    message += "Failed Features titles:\n"
    for scenario in failed_scenarios:
        message += f"- {scenario.name}\n"

    # Payload for Microsoft Teams
    payload = {
        "@type": "MessageCard",
        "@context": "Bee-links",
        "summary": "Test Automation Report",
        "title": "Notification From Software Quality Automation Team",
        "text": message
    }

    # Send POST request to Teams webhook
    response = requests.post(webhook_url, json=payload)

    if response.status_code == 200:
        print("Report sent to Teams Automation-Report channel successfully.")
    else:
        print(f"Failed to send message to Teams. Status code: {response.status_code}")
""")
            print(f"Created utilities file: {utilities_file_path}")
        else:
            print(f"Utilities file {utilities_file_path} already exists.")
    except Exception as e:
        print(f"Error creating methods folder: {str(e)}")

def create_configuration_file():
    try:
        configuration_file_path = "configuration.py"
        if not os.path.exists(configuration_file_path):
            with open(configuration_file_path, 'w') as file:
                file.write("""class configuration_system:
    webhook_url = "https://hulhub2.webhook.office.com/webhookb2/ddb52dda-66af-4d7f-a9c7-83683d8746ca@26521256-a7de-4702-a9f8-eace52025924/IncomingWebhook/9324409e882945178e9e72694a7a35cb/ae996ba4-1839-42f7-a024-a875284e262e"
""")
            print(f"Created configuration file: {configuration_file_path}")
        else:
            print(f"Configuration file {configuration_file_path} already exists.")
    except Exception as e:
        print(f"Error creating configuration file: {str(e)}")

def create_run_testcases_script():
    try:
        script_content = """import os
import subprocess
from datetime import datetime
import http.server
import socketserver
import threading
import webbrowser
import time
from features.steps.BeelinksTickets import generate_random_string

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
"""
        with open("run-testcases.py", 'w') as file:
            file.write(script_content)
        print("Created run-testcases.py script.")
    except Exception as e:
        print(f"Error creating run-testcases.py script: {str(e)}")

# Execute setup functions
install_python()
install_pycharm()
install_dependencies()
setup_allure()
install_java()
create_elements_folder()
create_features_folder()
create_methods_folder()
create_configuration_file()
