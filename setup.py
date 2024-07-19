lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII = Exception, str, print, open

import subprocess as IIIIIllllIlllI
import os as llllIlllIIIlIl
import sys as llllIIIlIlllll
import urllib.request as lllIllllIlIlII
import zipfile as IIllIIIllllllI
import shutil as lIIIIIlIlIlllI

def lIllllIlllIIIllIII(llIIllIIIIlIlllIII):
    try:
        lIIIIIlllllIIIIlIl = IIIIIllllIlllI.run(llIIllIIIIlIlllIII, shell=True, text=True, capture_output=True)
        if lIIIIIlllllIIIIlIl.returncode != 0:
            lllllllllllllIl(f'Error executing command: {llIIllIIIIlIlllIII}\n{lIIIIIlllllIIIIlIl.stderr}')
        else:
            lllllllllllllIl(f'Executed command: {llIIllIIIIlIlllIII}\n{lIIIIIlllllIIIIlIl.stdout}')
    except lllllllllllllll as IllIIllIllllIIIllI:
        lllllllllllllIl(f'Exception executing command: {llIIllIIIIlIlllIII}\n{llllllllllllllI(IllIIllIllllIIIllI)}')

def IllIIIllIllIlllIlI():
    lllllllllllllIl('Python installation skipped. Please ensure Python is installed.')

def lIIIIIlIllIlllllIl():
    lllllllllllllIl('Please download and install PyCharm from https://www.jetbrains.com/pycharm/download/')

def IIlIlIllllIIIlIIIl():
    IllllIIlIIIIllIIII = ['selenium', 'webdriver_manager', 'allure-behave', 'requests']
    for IlIIlIIllIllIlIllI in IllllIIlIIIIllIIII:
        lllllllllllllIl(f'Installing {IlIIlIIllIllIlIllI}...')
        lIllllIlllIIIllIII(f'pip install {IlIIlIIllIllIlIllI}')

def lIlllIlllIIIIlIlll():
    try:
        IIIIIIlllIIlllIIIl = 'https://github.com/allure-framework/allure2/releases/download/2.13.9/allure-2.13.9.zip'
        llIllIIIllllIIlIIl = 'allure.zip'
        IIllIIlIllIlIlIlll = 'allure'
        if llllIlllIIIlIl.path.exists(IIllIIlIllIlIlIlll):
            lllllllllllllIl('Allure already exists. Skipping download.')
        else:
            lllllllllllllIl('Downloading Allure...')
            lllllllllllllIl("If setting up the Allure path fails due to access permissions, please set it up manually. Go to Environment Variables, find the 'Path' variable, and add the Allure path up to the 'bin' directory. You can verify the setup by running allure --version in the command prompt")
            urllib.request.urlretrieve(IIIIIIlllIIlllIIIl, llIllIIIllllIIlIIl)
            lllllllllllllIl('Extracting Allure...')
            with IIllIIIllllllI.ZipFile(llIllIIIllllIIlIIl, 'r') as lIlllIlIlIIIIIllIl:
                lIlllIlIlIIIIIllIl.extractall(IIllIIlIllIlIlIlll)
            lIIIIIIIIlllIIIIIl = llllIlllIIIlIl.environ.get('ProgramFiles', 'C:\\Program Files')
            lIIIlIlIllllllIIll = llllIlllIIIlIl.path.join(lIIIIIIIIlllIIIIIl, 'allure')
            if llllIlllIIIlIl.path.exists(lIIIlIlIllllllIIll):
                lIIIIIlIlIlllI.rmtree(lIIIlIlIllllllIIll)
            lIIIIIlIlIlllI.move(IIllIIlIllIlIlIlll, lIIIlIlIllllllIIll)
            llllIlllIIIlIl.environ['PATH'] += llllIlllIIIlIl.pathsep + llllIlllIIIlIl.path.join(lIIIlIlIllllllIIll, 'bin')
            lllllllllllllIl('Allure installed and PATH updated.')
        IIllIlIIIIlIIlllll()
    except lllllllllllllll as IllIIllIllllIIIllI:
        lllllllllllllIl(f'Error setting up Allure: {llllllllllllllI(IllIIllIllllIIIllI)}')
        lllllllllllllIl("setting up the Allure path fails due to access permissions, please set it up manually. Go to Environment Variables, find the 'Path' variable, and add the Allure path up to the 'bin' directory. You can verify the setup by running allure --version in the command prompt")

def lIllIlIllIllIIIlIl():
    try:
        llllIIIlIlIlIlIIII = 'C:\\Program Files\\Java\\jdk-17'
        if llllIlllIIIlIl.path.exists(llllIIIlIlIlIlIIII):
            lllllllllllllIl('Java is already installed.')
        else:
            IlIIIIIlllIlIIIlll = 'https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe'
            llIlIllllIlIlIllIl = 'jdk_installer.exe'
            lllllllllllllIl('Downloading Java...')
            urllib.request.urlretrieve(IlIIIIIlllIlIIIlll, llIlIllllIlIlIllIl)
            lllllllllllllIl('Running Java installer...')
            lIllllIlllIIIllIII(llIlIllllIlIlIllIl)
            llllIlllIIIlIl.environ['JAVA_HOME'] = llllIIIlIlIlIlIIII
            llllIlllIIIlIl.environ['PATH'] += llllIlllIIIlIl.pathsep + llllIlllIIIlIl.path.join(llllIIIlIlIlIlIIII, 'bin')
            lllllllllllllIl('Java installed and JAVA_HOME set.')
    except lllllllllllllll as IllIIllIllllIIIllI:
        lllllllllllllIl(f'Error installing Java: {llllllllllllllI(IllIIllIllllIIIllI)}')

def IlIIIIlIIIIIIIlIlI():
    try:
        llllIlIIllIIlIlIIl = 'elements'
        if not llllIlllIIIlIl.path.exists(llllIlIIllIIlIlIIl):
            llllIlllIIIlIl.makedirs(llllIlIIllIIlIlIIl)
            lllllllllllllIl(f'Created folder: {llllIlIIllIIlIlIIl}')
        IIIllIIIIIIlllllIl = llllIlllIIIlIl.path.join(llllIlIIllIIlIlIIl, 'sample_element.py')
        if not llllIlllIIIlIl.path.exists(IIIllIIIIIIlllllIl):
            with lllllllllllllII(IIIllIIIIIIlllllIl, 'w') as lIlIlIlllIIIIlIIIl:
                lIlIlIlllIIIIlIIIl.write('# Add page elements here\n')
                lIlIlIlllIIIIlIIIl.write('class elements:\n')
                lIlIlIlllIIIIlIIIl.write('    google_search = "q"\n')
            lllllllllllllIl(f'Created sample file: {IIIllIIIIIIlllllIl}')
        else:
            lllllllllllllIl(f'Sample file {IIIllIIIIIIlllllIl} already exists.')
    except lllllllllllllll as IllIIllIllllIIIllI:
        lllllllllllllIl(f'Error creating elements folder: {llllllllllllllI(IllIIllIllllIIIllI)}')

def IlIIIlIlllIlIIlllI():
    try:
        IllIllIlllllIllIII = 'features'
        IIllIlIIIIlIlIlllI = llllIlllIIIlIl.path.join(IllIllIlllllIllIII, 'steps')
        if not llllIlllIIIlIl.path.exists(IllIllIlllllIllIII):
            llllIlllIIIlIl.makedirs(IllIllIlllllIllIII)
            lllllllllllllIl(f'Created folder: {IllIllIlllllIllIII}')
        if not llllIlllIIIlIl.path.exists(IIllIlIIIIlIlIlllI):
            llllIlllIIIlIl.makedirs(IIllIlIIIIlIlIlllI)
            lllllllllllllIl(f'Created folder: {IIllIlIIIIlIlIlllI}')
        llIIIIlIllllllIIll = llllIlllIIIlIl.path.join(IllIllIlllllIllIII, 'search_google.feature')
        if not llllIlllIIIlIl.path.exists(llIIIIlIllllllIIll):
            with lllllllllllllII(llIIIIlIllllllIIll, 'w') as lIlIlIlllIIIIlIIIl:
                lIlIlIlllIIIIlIIIl.write('Feature: Search Google\n\n@smoke\nScenario: Search for kamran ghaffar on Google and click the first link\n    Given the user is on the Google homepage\n    When the user searches for kamran ghaffar\n    Then the user clicks on the first search result\n')
            lllllllllllllIl(f'Created feature file: {llIIIIlIllllllIIll}')
        else:
            lllllllllllllIl(f'Feature file {llIIIIlIllllllIIll} already exists.')
        IIIlIlIllIllllIIIl = llllIlllIIIlIl.path.join(IIllIlIIIIlIlIlllI, 'search_google_steps.py')
        if not llllIlllIIIlIl.path.exists(IIIlIlIllIllllIIIl):
            with lllllllllllllII(IIIlIlIllIllllIIIl, 'w') as lIlIlIlllIIIIlIIIl:
                lIlIlIlllIIIIlIIIl.write('from behave import given, when, then\nfrom selenium.webdriver.common.by import By\nfrom selenium.webdriver.common.keys import Keys\nfrom elements.sample_element import elements\nfrom configuration import *\n\n@given(\'the user is on the Google homepage\')\ndef step_given_user_on_google_homepage(context):\n    context.driver.get(configuration_system.URL)\n\n@when(\'the user searches for kamran ghaffar\')\ndef step_when_user_searches(context):\n    search_box = context.driver.find_element(By.NAME, elements.google_search)\n    search_box.send_keys("kamran ghaffar" + Keys.RETURN)\n\n@then(\'the user clicks on the first search result\')\ndef step_then_click_first_result(context):\n    first_result = context.driver.find_element(By.CSS_SELECTOR, \'h3\')\n    first_result.click()\n')
            lllllllllllllIl(f'Created steps file: {IIIlIlIllIllllIIIl}')
        else:
            lllllllllllllIl(f'Steps file {IIIlIlIllIllllIIIl} already exists.')
        llIIIlIlllIIlIlIII = llllIlllIIIlIl.path.join(IllIllIlllllIllIII, 'environment.py')
        if not llllIlllIIIlIl.path.exists(llIIIlIlllIIlIlIII):
            with lllllllllllllII(llIIIlIlllIIlIlIII, 'w') as lIlIlIlllIIIIlIIIl:
                lIlIlIlllIIIIlIIIl.write('from selenium import webdriver\nfrom selenium.webdriver.chrome.service import Service\nfrom webdriver_manager.chrome import ChromeDriverManager\nfrom configuration import configuration_system\nfrom methods.utilities import *\n\ndef before_all(context):\n    # Executed once before any scenarios are run\n    pass\n\ndef before_feature(context, feature):\n    # Executed before each feature is run\n    pass\n\ndef before_scenario(context, scenario):\n    # for Headless mode\n    chrome_options = webdriver.ChromeOptions()\n    #chrome_options.add_argument("--headless")\n\n    # Initialize the Chrome service\n    service = Service(ChromeDriverManager().install())\n\n    # Initialize the WebDriver with options and service\n    context.driver = webdriver.Chrome(service=service, options=chrome_options)\n\n    # Set window size and implicit wait time\n    context.driver.maximize_window()\n    context.driver.implicitly_wait(30)\n\ndef after_scenario(context, scenario):\n    # Close the browser after each scenario\n    context.driver.quit()\n\ndef after_step(context, step):\n    if configuration_system.screenshot:\n        step_capture_screenshot(context)\n\ndef after_feature(context, feature):\n    # Executed after each feature is run\n    pass\n\ndef after_all(context):\n    # Executed once after all scenarios are run\n    passed_scenarios = [scenario for scenario in context._runner.features if scenario.status.name == "passed"]\n    failed_scenarios = [scenario for scenario in context._runner.features if scenario.status.name == "failed"]\n    if configuration_system.report:\n        send_teams_webhook(passed_scenarios, failed_scenarios)\n')
            lllllllllllllIl(f'Created environment file: {llIIIlIlllIIlIlIII}')
        else:
            lllllllllllllIl(f'Environment file {llIIIlIlllIIlIlIII} already exists.')
    except lllllllllllllll as IllIIllIllllIIIllI:
        lllllllllllllIl(f'Error creating features folder: {llllllllllllllI(IllIIllIllllIIIllI)}')

def IIIIIIIIlIlIlIIIIl():
    try:
        llIIllllllIIIIllll = 'methods'
        if not llllIlllIIIlIl.path.exists(llIIllllllIIIIllll):
            llllIlllIIIlIl.makedirs(llIIllllllIIIIllll)
            lllllllllllllIl(f'Created folder: {llIIllllllIIIIllll}')
        lIIIllIlllllIllIll = llllIlllIIIlIl.path.join(llIIllllllIIIIllll, 'utilities.py')
        if not llllIlllIIIlIl.path.exists(lIIIllIlllllIllIll):
            with lllllllllllllII(lIIIllIlllllIllIll, 'w') as lIlIlIlllIIIIlIIIl:
                lIlIlIlllIIIIlIIIl.write('import random\nimport os\nimport allure\nimport requests\nfrom selenium.common.exceptions import NoSuchElementException\nimport configuration\n\ndef step_capture_screenshot(context):\n    # Capture screenshot and save it in the "screenshots" directory\n    screenshot_dir = "screenshots"\n    os.makedirs(screenshot_dir, exist_ok=True)\n    random_3_digit_number = random.randint(100, 999)\n    ran_num = str(random_3_digit_number)\n    screenshot_name = "screenshot" + ran_num + ".png"\n    screenshot_path = os.path.join(screenshot_dir, screenshot_name)\n    context.driver.save_screenshot(screenshot_path)\n    # Attach the screenshot to the Allure report\n    with allure.step(\'Attach Screenshot\'):\n        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG, name=screenshot_name)\n\ndef trigger_webhook(total_failures, failure_details):\n    # Use the correct webhook URL from configuration\n    teams_webhook_url = configuration.configuration_system.webhook_url\n    payload = {\n        "@type": "MessageCard",\n        "@context": "",\n        "summary": "Test Automation Failure",\n        "title": "Failed Failed Failed!!!!",\n        "sections": [{\n            "activityTitle": "Test Automation Failure Details",\n            "activitySubtitle": f"Total Failures: {total_failures}",\n            "facts": [{\n                "name": "Total Failures",\n                "value": total_failures\n            }] + [\n                         {\n                             "name": f"Failure {i + 1}",\n                             "value": detail\n                         } for i, detail in enumerate(failure_details)\n                     ]\n        }]\n    }\n    try:\n        response = requests.post(teams_webhook_url, json=payload)\n        response.raise_for_status()  # Raise exception for HTTP errors\n    except Exception as e:\n        print("Error triggering webhook:", e)\n\ndef assert_element_exists(driver, by, locator, failure_details):\n    try:\n        driver.find_element(by, locator)\n    except NoSuchElementException:\n        failure_details.append(f"Element not found: {locator}")\n        total_failures = len(failure_details)\n        trigger_webhook(total_failures, failure_details)\n        raise AssertionError(f"Element not found: {locator}")\n\ndef send_teams_webhook(passed_scenarios, failed_scenarios):\n    # Teams webhook URL\n    webhook_url = configuration.configuration_system.webhook_url\n\n    # Format message for Teams\n    message = f"Total passed Features: {len(passed_scenarios)}"\n    message += f"Total failed Features: {len(failed_scenarios)}"\n    message += "Failed Features titles:"\n    for scenario in failed_scenarios:\n        message += f"- {scenario.name}"\n\n    # Payload for Microsoft Teams\n    payload = {\n        "@type": "MessageCard",\n        "@context": "Bee-links",\n        "summary": "Test Automation Report",\n        "title": "Notification From Software Quality Automation Team",\n        "text": message\n    }\n\n    # Send POST request to Teams webhook\n    response = requests.post(webhook_url, json=payload)\n\n    if response.status_code == 200:\n        print("Report sent to Teams Automation-Report channel successfully.")\n    else:\n        print(f"Failed to send message to Teams. Status code: {response.status_code}")\n')
            lllllllllllllIl(f'Created utilities file: {lIIIllIlllllIllIll}')
        else:
            lllllllllllllIl(f'Utilities file {lIIIllIlllllIllIll} already exists.')
    except lllllllllllllll as IllIIllIllllIIIllI:
        lllllllllllllIl(f'Error creating methods folder: {llllllllllllllI(IllIIllIllllIIIllI)}')

def IlIIIIIIlIllIlIlIl():
    try:
        IIIlIlllIlIlIIlIll = 'configuration.py'
        if not llllIlllIIIlIl.path.exists(IIIlIlllIlIlIIlIll):
            with lllllllllllllII(IIIlIlllIlIlIIlIll, 'w') as lIlIlIlllIIIIlIIIl:
                lIlIlIlllIIIIlIIIl.write('class configuration_system:\n    webhook_url = "add webhook here"\n    screenshot = True\n    report = False\n    URL = "https://www.google.com"\n\n')
            lllllllllllllIl(f'Created configuration file: {IIIlIlllIlIlIIlIll}')
        else:
            lllllllllllllIl(f'Configuration file {IIIlIlllIlIlIIlIll} already exists.')
    except lllllllllllllll as IllIIllIllllIIIllI:
        lllllllllllllIl(f'Error creating configuration file: {llllllllllllllI(IllIIllIllllIIIllI)}')

def IIllIlIIIIlIIlllll():
    try:
        lllllllllIllIllIll = 'import os\nimport subprocess\nfrom datetime import datetime\nimport http.server\nimport socketserver\nimport threading\nimport webbrowser\nimport time\nimport random\nimport string\n\ndef generate_random_string(length=10):\n    return \'\'.join(random.choices(string.ascii_letters, k=length))\n\nrandom_id = generate_random_string(3)\n\ndef run_tests_and_generate_report():\n    # Create a unique folder with today\'s date\n    today = datetime.now().strftime("%Y-%m-%d")\n    results_dir = f"allure_results_{today}_{random_id}"\n    report_dir = f"TestReport_{today}_{random_id}/allure_report"\n\n    # Create directories if they don\'t exist\n    os.makedirs(results_dir, exist_ok=True)\n    os.makedirs(report_dir, exist_ok=True)\n\n    # Define commands\n    behave_command = ["behave", "--tags=@smoke", "-f", "allure_behave.formatter:AllureFormatter", "-o", results_dir]\n    allure_generate_command = ["allure", "generate", results_dir, "-o", report_dir, "--clean"]\n\n    try:\n        # Run behave command to generate allure results\n        subprocess.run(behave_command, shell=True, check=True)\n    except subprocess.CalledProcessError as e:\n        print(f"Behave command failed with exit code {e.returncode}")\n\n    # Generate the allure report\n    subprocess.run(allure_generate_command, shell=True, check=True)\n\n    # Serve the generated report\n    serve_report(report_dir)\n\ndef serve_report(report_dir):\n    # Define the handler to serve files from the report directory\n    handler = http.server.SimpleHTTPRequestHandler\n    os.chdir(report_dir)\n\n    # Define the server\n    PORT = 8000\n    httpd = socketserver.TCPServer(("", PORT), handler)\n\n    # Open the report in the default web browser\n    webbrowser.open(f"http://localhost:{PORT}/index.html")\n\n    # Start the server\n    server_thread = threading.Thread(target=httpd.serve_forever)\n    server_thread.start()\n\n    # Allow some time for the browser to load the report\n    time.sleep(20)\n\n    # Shutdown the server\n    httpd.shutdown()\n    server_thread.join()\n\nif __name__ == "__main__":\n    run_tests_and_generate_report()\n'
        with lllllllllllllII('run-testcases.py', 'w') as lIlIlIlllIIIIlIIIl:
            lIlIlIlllIIIIlIIIl.write(lllllllllIllIllIll)
        lllllllllllllIl('Created run-testcases.py script.')
    except lllllllllllllll as IllIIllIllllIIIllI:
        lllllllllllllIl(f'Error creating run-testcases.py script: {llllllllllllllI(IllIIllIllllIIIllI)}')
IllIIIllIllIlllIlI()
lIIIIIlIllIlllllIl()
IIlIlIllllIIIlIIIl()
lIlllIlllIIIIlIlll()
lIllIlIllIllIIIlIl()
IlIIIIlIIIIIIIlIlI()
IlIIIlIlllIlIIlllI()
IIIIIIIIlIlIlIIIIl()
IlIIIIIIlIllIlIlIl()
IIllIlIIIIlIIlllll()
