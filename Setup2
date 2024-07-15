lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII = open, Exception, print, str

import subprocess as lIllIlIIIllllI
import os as IIIllIlIIlllll
import sys as lllIlllIlIllII
import urllib.request as lIIllIIIlIlIlI
import zipfile as llllIlllIlIIll
import shutil as IIllIIlIIIllIl

def lIIIlIlllllIlIlIlI(llIllIllllIlIlllll):
    try:
        IIIllIIIlIllIlIIll = lIllIlIIIllllI.run(llIllIllllIlIlllll, shell=True, text=True, capture_output=True)
        if IIIllIIIlIllIlIIll.returncode != 0:
            lllllllllllllIl(f'Error executing command: {llIllIllllIlIlllll}\n{IIIllIIIlIllIlIIll.stderr}')
        else:
            lllllllllllllIl(f'Executed command: {llIllIllllIlIlllll}\n{IIIllIIIlIllIlIIll.stdout}')
    except llllllllllllllI as llIIIllIlIllIIIllI:
        lllllllllllllIl(f'Exception executing command: {llIllIllllIlIlllll}\n{lllllllllllllII(llIIIllIlIllIIIllI)}')

def llllllllIlllllIlII():
    lllllllllllllIl('Python installation skipped. Please ensure Python is installed.')

def IllIIlIlIIlIlIIIll():
    lllllllllllllIl('Please download and install PyCharm from https://www.jetbrains.com/pycharm/download/')

def lllIIIlllllIlIIIII():
    IllllllIIIlllIIlIl = ['selenium', 'webdriver_manager', 'allure-behave', 'requests']
    for lllIIIllllIIIIllII in IllllllIIIlllIIlIl:
        lllllllllllllIl(f'Installing {lllIIIllllIIIIllII}...')
        lIIIlIlllllIlIlIlI(f'pip install {lllIIIllllIIIIllII}')

def IIlIIIllllllIIIIll():
    try:
        llIllIlIIlIIIIlIIl = 'https://github.com/allure-framework/allure2/releases/download/2.13.9/allure-2.13.9.zip'
        llIIlIIlIllIllllll = 'allure.zip'
        IIIlIllIIllllIlIll = 'allure'
        if IIIllIlIIlllll.path.exists(IIIlIllIIllllIlIll):
            lllllllllllllIl('Allure already exists. Skipping download.')
        else:
            lllllllllllllIl('Downloading Allure...')
            lllllllllllllIl("If setting up the Allure path fails due to access permissions, please set it up manually. Go to Environment Variables, find the 'Path' variable, and add the Allure path up to the 'bin' directory. You can verify the setup by running allure --version in the command prompt")
            urllib.request.urlretrieve(llIllIlIIlIIIIlIIl, llIIlIIlIllIllllll)
            lllllllllllllIl('Extracting Allure...')
            with llllIlllIlIIll.ZipFile(llIIlIIlIllIllllll, 'r') as IIIIlIlIlIllIllIII:
                IIIIlIlIlIllIllIII.extractall(IIIlIllIIllllIlIll)
            IIlIlllIlIlIlIIlIl = IIIllIlIIlllll.environ.get('ProgramFiles', 'C:\\Program Files')
            llIIIIllllIIlIllll = IIIllIlIIlllll.path.join(IIlIlllIlIlIlIIlIl, 'allure')
            if IIIllIlIIlllll.path.exists(llIIIIllllIIlIllll):
                IIllIIlIIIllIl.rmtree(llIIIIllllIIlIllll)
            IIllIIlIIIllIl.move(IIIlIllIIllllIlIll, llIIIIllllIIlIllll)
            IIIllIlIIlllll.environ['PATH'] += IIIllIlIIlllll.pathsep + IIIllIlIIlllll.path.join(llIIIIllllIIlIllll, 'bin')
            lllllllllllllIl('Allure installed and PATH updated.')
        lIlllllIlIIIIIIIll()
    except llllllllllllllI as llIIIllIlIllIIIllI:
        lllllllllllllIl(f'Error setting up Allure: {lllllllllllllII(llIIIllIlIllIIIllI)}')
        lllllllllllllIl("setting up the Allure path fails due to access permissions, please set it up manually. Go to Environment Variables, find the 'Path' variable, and add the Allure path up to the 'bin' directory. You can verify the setup by running allure --version in the command prompt")

def IllIIllIIIIIIIIlll():
    try:
        lIllIIIllIIllllIII = 'C:\\Program Files\\Java\\jdk-17'
        if IIIllIlIIlllll.path.exists(lIllIIIllIIllllIII):
            lllllllllllllIl('Java is already installed.')
        else:
            IIlIllIllllllllIlI = 'https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe'
            lllIlIIIIIIlllIlll = 'jdk_installer.exe'
            lllllllllllllIl('Downloading Java...')
            urllib.request.urlretrieve(IIlIllIllllllllIlI, lllIlIIIIIIlllIlll)
            lllllllllllllIl('Running Java installer...')
            lIIIlIlllllIlIlIlI(lllIlIIIIIIlllIlll)
            IIIllIlIIlllll.environ['JAVA_HOME'] = lIllIIIllIIllllIII
            IIIllIlIIlllll.environ['PATH'] += IIIllIlIIlllll.pathsep + IIIllIlIIlllll.path.join(lIllIIIllIIllllIII, 'bin')
            lllllllllllllIl('Java installed and JAVA_HOME set.')
    except llllllllllllllI as llIIIllIlIllIIIllI:
        lllllllllllllIl(f'Error installing Java: {lllllllllllllII(llIIIllIlIllIIIllI)}')

def IlIIlIIIlllIlIllIl():
    try:
        IlIIllIIIIlIIlllIl = 'elements'
        if not IIIllIlIIlllll.path.exists(IlIIllIIIIlIIlllIl):
            IIIllIlIIlllll.makedirs(IlIIllIIIIlIIlllIl)
            lllllllllllllIl(f'Created folder: {IlIIllIIIIlIIlllIl}')
        IlIIlIIIIllIllIllI = IIIllIlIIlllll.path.join(IlIIllIIIIlIIlllIl, 'sample_element.py')
        if not IIIllIlIIlllll.path.exists(IlIIlIIIIllIllIllI):
            with lllllllllllllll(IlIIlIIIIllIllIllI, 'w') as lIIlIIIllllIlllIll:
                lIIlIIIllllIlllIll.write('# Add page elements here\n')
            lllllllllllllIl(f'Created sample file: {IlIIlIIIIllIllIllI}')
        else:
            lllllllllllllIl(f'Sample file {IlIIlIIIIllIllIllI} already exists.')
    except llllllllllllllI as llIIIllIlIllIIIllI:
        lllllllllllllIl(f'Error creating elements folder: {lllllllllllllII(llIIIllIlIllIIIllI)}')

def llIIIlIllllIIIlIIl():
    try:
        IlIlIIIIlIllIlIIlI = 'features'
        IIIlllIIllllIIlIIl = IIIllIlIIlllll.path.join(IlIlIIIIlIllIlIIlI, 'steps')
        if not IIIllIlIIlllll.path.exists(IlIlIIIIlIllIlIIlI):
            IIIllIlIIlllll.makedirs(IlIlIIIIlIllIlIIlI)
            lllllllllllllIl(f'Created folder: {IlIlIIIIlIllIlIIlI}')
        if not IIIllIlIIlllll.path.exists(IIIlllIIllllIIlIIl):
            IIIllIlIIlllll.makedirs(IIIlllIIllllIIlIIl)
            lllllllllllllIl(f'Created folder: {IIIlllIIllllIIlIIl}')
        lllllIlIlIllllllIl = IIIllIlIIlllll.path.join(IlIlIIIIlIllIlIIlI, 'search_google.feature')
        if not IIIllIlIIlllll.path.exists(lllllIlIlIllllllIl):
            with lllllllllllllll(lllllIlIlIllllllIl, 'w') as lIIlIIIllllIlllIll:
                lIIlIIIllllIlllIll.write('Feature: Search Google\n\n@smoke\nScenario: Search for kamran ghaffar on Google and click the first link\n    Given the user is on the Google homepage\n    When the user searches for kamran ghaffar\n    Then the user clicks on the first search result\n')
            lllllllllllllIl(f'Created feature file: {lllllIlIlIllllllIl}')
        else:
            lllllllllllllIl(f'Feature file {lllllIlIlIllllllIl} already exists.')
        IIIIllIIlIlIIIIlII = IIIllIlIIlllll.path.join(IIIlllIIllllIIlIIl, 'search_google_steps.py')
        if not IIIllIlIIlllll.path.exists(IIIIllIIlIlIIIIlII):
            with lllllllllllllll(IIIIllIIlIlIIIIlII, 'w') as lIIlIIIllllIlllIll:
                lIIlIIIllllIlllIll.write('from behave import given, when, then\nfrom selenium.webdriver.common.by import By\nfrom selenium.webdriver.common.keys import Keys\n\n@given(\'the user is on the Google homepage\')\ndef step_given_user_on_google_homepage(context):\n    context.driver.get("https://www.google.com")\n\n@when(\'the user searches for kamran ghaffar\')\ndef step_when_user_searches(context):\n    search_box = context.driver.find_element(By.NAME, "q")\n    search_box.send_keys("kamran ghaffar" + Keys.RETURN)\n\n@then(\'the user clicks on the first search result\')\ndef step_then_click_first_result(context):\n    first_result = context.driver.find_element(By.CSS_SELECTOR, \'h3\')\n    first_result.click()\n')
            lllllllllllllIl(f'Created steps file: {IIIIllIIlIlIIIIlII}')
        else:
            lllllllllllllIl(f'Steps file {IIIIllIIlIlIIIIlII} already exists.')
        lllllIlllIllIlIlII = IIIllIlIIlllll.path.join(IlIlIIIIlIllIlIIlI, 'environment.py')
        if not IIIllIlIIlllll.path.exists(lllllIlllIllIlIlII):
            with lllllllllllllll(lllllIlllIllIlIlII, 'w') as lIIlIIIllllIlllIll:
                lIIlIIIllllIlllIll.write('from selenium import webdriver\nfrom selenium.webdriver.chrome.service import Service\nfrom webdriver_manager.chrome import ChromeDriverManager\nfrom configuration import configuration_system\nfrom methods.utilities import *\n\ndef before_all(context):\n    # Executed once before any scenarios are run\n    pass\n\ndef before_feature(context, feature):\n    # Executed before each feature is run\n    pass\n\ndef before_scenario(context, scenario):\n    # for Headless mode\n    chrome_options = webdriver.ChromeOptions()\n    #chrome_options.add_argument("--headless")\n\n    # Initialize the Chrome service\n    service = Service(ChromeDriverManager().install())\n\n    # Initialize the WebDriver with options and service\n    context.driver = webdriver.Chrome(service=service, options=chrome_options)\n\n    # Set window size and implicit wait time\n    context.driver.maximize_window()\n    context.driver.implicitly_wait(30)\n\ndef after_scenario(context, scenario):\n    # Close the browser after each scenario\n    context.driver.quit()\n\ndef after_step(context, step):\n    if configuration_system.screenshot:\n        step_capture_screenshot(context)\n\ndef after_feature(context, feature):\n    # Executed after each feature is run\n    pass\n\ndef after_all(context):\n    # Executed once after all scenarios are run\n    passed_scenarios = [scenario for scenario in context._runner.features if scenario.status.name == "passed"]\n    failed_scenarios = [scenario for scenario in context._runner.features if scenario.status.name == "failed"]\n    if configuration_system.report:\n        send_teams_webhook(passed_scenarios, failed_scenarios)\n')
            lllllllllllllIl(f'Created environment file: {lllllIlllIllIlIlII}')
        else:
            lllllllllllllIl(f'Environment file {lllllIlllIllIlIlII} already exists.')
    except llllllllllllllI as llIIIllIlIllIIIllI:
        lllllllllllllIl(f'Error creating features folder: {lllllllllllllII(llIIIllIlIllIIIllI)}')

def lIIlllllIIlIlIllll():
    try:
        IllIlIlIIlllIIIlIl = 'methods'
        if not IIIllIlIIlllll.path.exists(IllIlIlIIlllIIIlIl):
            IIIllIlIIlllll.makedirs(IllIlIlIIlllIIIlIl)
            lllllllllllllIl(f'Created folder: {IllIlIlIIlllIIIlIl}')
        lIIIIIIlllIIlIllIl = IIIllIlIIlllll.path.join(IllIlIlIIlllIIIlIl, 'utilities.py')
        if not IIIllIlIIlllll.path.exists(lIIIIIIlllIIlIllIl):
            with lllllllllllllll(lIIIIIIlllIIlIllIl, 'w') as lIIlIIIllllIlllIll:
                lIIlIIIllllIlllIll.write('import random\nimport os\nimport allure\nimport requests\nfrom selenium.common.exceptions import NoSuchElementException\nimport configuration\n\ndef step_capture_screenshot(context):\n    # Capture screenshot and save it in the "screenshots" directory\n    screenshot_dir = "screenshots"\n    os.makedirs(screenshot_dir, exist_ok=True)\n    random_3_digit_number = random.randint(100, 999)\n    ran_num = str(random_3_digit_number)\n    screenshot_name = "screenshot" + ran_num + ".png"\n    screenshot_path = os.path.join(screenshot_dir, screenshot_name)\n    context.driver.save_screenshot(screenshot_path)\n    # Attach the screenshot to the Allure report\n    with allure.step(\'Attach Screenshot\'):\n        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG, name=screenshot_name)\n\ndef trigger_webhook(total_failures, failure_details):\n    # Use the correct webhook URL from configuration\n    teams_webhook_url = configuration.configuration_system.webhook_url\n    payload = {\n        "@type": "MessageCard",\n        "@context": "",\n        "summary": "Test Automation Failure",\n        "title": "Failed Failed Failed!!!!",\n        "sections": [{\n            "activityTitle": "Test Automation Failure Details",\n            "activitySubtitle": f"Total Failures: {total_failures}",\n            "facts": [{\n                "name": "Total Failures",\n                "value": total_failures\n            }] + [\n                         {\n                             "name": f"Failure {i + 1}",\n                             "value": detail\n                         } for i, detail in enumerate(failure_details)\n                     ]\n        }]\n    }\n    try:\n        response = requests.post(teams_webhook_url, json=payload)\n        response.raise_for_status()  # Raise exception for HTTP errors\n    except Exception as e:\n        print("Error triggering webhook:", e)\n\ndef assert_element_exists(driver, by, locator, failure_details):\n    try:\n        driver.find_element(by, locator)\n    except NoSuchElementException:\n        failure_details.append(f"Element not found: {locator}")\n        total_failures = len(failure_details)\n        trigger_webhook(total_failures, failure_details)\n        raise AssertionError(f"Element not found: {locator}")\n\ndef send_teams_webhook(passed_scenarios, failed_scenarios):\n    # Teams webhook URL\n    webhook_url = configuration.configuration_system.webhook_url\n\n    # Format message for Teams\n    message = f"Total passed Features: {len(passed_scenarios)}"\n    message += f"Total failed Features: {len(failed_scenarios)}"\n    message += "Failed Features titles:"\n    for scenario in failed_scenarios:\n        message += f"- {scenario.name}"\n\n    # Payload for Microsoft Teams\n    payload = {\n        "@type": "MessageCard",\n        "@context": "Bee-links",\n        "summary": "Test Automation Report",\n        "title": "Notification From Software Quality Automation Team",\n        "text": message\n    }\n\n    # Send POST request to Teams webhook\n    response = requests.post(webhook_url, json=payload)\n\n    if response.status_code == 200:\n        print("Report sent to Teams Automation-Report channel successfully.")\n    else:\n        print(f"Failed to send message to Teams. Status code: {response.status_code}")\n')
            lllllllllllllIl(f'Created utilities file: {lIIIIIIlllIIlIllIl}')
        else:
            lllllllllllllIl(f'Utilities file {lIIIIIIlllIIlIllIl} already exists.')
    except llllllllllllllI as llIIIllIlIllIIIllI:
        lllllllllllllIl(f'Error creating methods folder: {lllllllllllllII(llIIIllIlIllIIIllI)}')

def llIIlllIllllllIIII():
    try:
        IIIlllllIlllIlllIl = 'configuration.py'
        if not IIIllIlIIlllll.path.exists(IIIlllllIlllIlllIl):
            with lllllllllllllll(IIIlllllIlllIlllIl, 'w') as lIIlIIIllllIlllIll:
                lIIlIIIllllIlllIll.write('class configuration_system:\n    webhook_url = "add webhook here"\n    screenshot = True\n    report = False\n    \n')
            lllllllllllllIl(f'Created configuration file: {IIIlllllIlllIlllIl}')
        else:
            lllllllllllllIl(f'Configuration file {IIIlllllIlllIlllIl} already exists.')
    except llllllllllllllI as llIIIllIlIllIIIllI:
        lllllllllllllIl(f'Error creating configuration file: {lllllllllllllII(llIIIllIlIllIIIllI)}')

def lIlllllIlIIIIIIIll():
    try:
        llIIlllIllIIlIIIII = 'import os\nimport subprocess\nfrom datetime import datetime\nimport http.server\nimport socketserver\nimport threading\nimport webbrowser\nimport time\nimport random\nimport string\n\ndef generate_random_string(length=10):\n    return \'\'.join(random.choices(string.ascii_letters, k=length))\n\nrandom_id = generate_random_string(3)\n\ndef run_tests_and_generate_report():\n    # Create a unique folder with today\'s date\n    today = datetime.now().strftime("%Y-%m-%d")\n    results_dir = f"allure_results_{today}_{random_id}"\n    report_dir = f"TestReport_{today}_{random_id}/allure_report"\n\n    # Create directories if they don\'t exist\n    os.makedirs(results_dir, exist_ok=True)\n    os.makedirs(report_dir, exist_ok=True)\n\n    # Define commands\n    behave_command = ["behave", "--tags=@smoke", "-f", "allure_behave.formatter:AllureFormatter", "-o", results_dir]\n    allure_generate_command = ["allure", "generate", results_dir, "-o", report_dir, "--clean"]\n\n    try:\n        # Run behave command to generate allure results\n        subprocess.run(behave_command, shell=True, check=True)\n    except subprocess.CalledProcessError as e:\n        print(f"Behave command failed with exit code {e.returncode}")\n\n    # Generate the allure report\n    subprocess.run(allure_generate_command, shell=True, check=True)\n\n    # Serve the generated report\n    serve_report(report_dir)\n\ndef serve_report(report_dir):\n    # Define the handler to serve files from the report directory\n    handler = http.server.SimpleHTTPRequestHandler\n    os.chdir(report_dir)\n\n    # Define the server\n    PORT = 8000\n    httpd = socketserver.TCPServer(("", PORT), handler)\n\n    # Open the report in the default web browser\n    webbrowser.open(f"http://localhost:{PORT}/index.html")\n\n    # Start the server\n    server_thread = threading.Thread(target=httpd.serve_forever)\n    server_thread.start()\n\n    # Allow some time for the browser to load the report\n    time.sleep(20)\n\n    # Shutdown the server\n    httpd.shutdown()\n    server_thread.join()\n\nif __name__ == "__main__":\n    run_tests_and_generate_report()\n'
        with lllllllllllllll('run-testcases.py', 'w') as lIIlIIIllllIlllIll:
            lIIlIIIllllIlllIll.write(llIIlllIllIIlIIIII)
        lllllllllllllIl('Created run-testcases.py script.')
    except llllllllllllllI as llIIIllIlIllIIIllI:
        lllllllllllllIl(f'Error creating run-testcases.py script: {lllllllllllllII(llIIIllIlIllIIIllI)}')
llllllllIlllllIlII()
IllIIlIlIIlIlIIIll()
lllIIIlllllIlIIIII()
IIlIIIllllllIIIIll()
IllIIllIIIIIIIIlll()
IlIIlIIIlllIlIllIl()
llIIIlIllllIIIlIIl()
lIIlllllIIlIlIllll()
llIIlllIllllllIIII()
lIlllllIlIIIIIIIll()
