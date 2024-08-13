lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII = open, Exception, print, str

import subprocess as IlIlIIlllllIII
import os as IlIIlIlllIllll
import sys as IIIlIIIllIllII
import urllib.request as llIIIIIllIIIlI
import zipfile as IlIllIIlIlIlIl
import shutil as llllllIIlIIlIl

def IIlIlIIIIIIllIIlII(llIIlIIllllIIlIIIl):
    try:
        lIIlIlllllIIlIIIII = IlIlIIlllllIII.run(llIIlIIllllIIlIIIl, shell=True, text=True, capture_output=True)
        if lIIlIlllllIIlIIIII.returncode != 0:
            lllllllllllllIl(f'Error executing command: {llIIlIIllllIIlIIIl}\n{lIIlIlllllIIlIIIII.stderr}')
        else:
            lllllllllllllIl(f'Executed command: {llIIlIIllllIIlIIIl}\n{lIIlIlllllIIlIIIII.stdout}')
    except llllllllllllllI as llIllIIIllIIllIlIl:
        lllllllllllllIl(f'Exception executing command: {llIIlIIllllIIlIIIl}\n{lllllllllllllII(llIllIIIllIIllIlIl)}')

def IIllllllIllIlllIlI():
    lllllllllllllIl('Python installation skipped. Please ensure Python is installed.')

def IIIIIIIllIIIlIllIl():
    lllllllllllllIl('Please download and install PyCharm from https://www.jetbrains.com/pycharm/download/')

def IllIIllllIlllIIlll():
    lllIllllIIlIlIIlIl = ['selenium', 'webdriver_manager', 'allure-behave', 'requests']
    for IlIIIIIlIlllIIlIII in lllIllllIIlIlIIlIl:
        lllllllllllllIl(f'Installing {IlIIIIIlIlllIIlIII}...')
        IIlIlIIIIIIllIIlII(f'pip install {IlIIIIIlIlllIIlIII}')

def IIlllIlIlIlIIlIllI():
    try:
        IlIlIIIIllIIIlIlII = 'https://github.com/allure-framework/allure2/releases/download/2.13.9/allure-2.13.9.zip'
        IllIllllllllllIIll = 'allure.zip'
        IIIIIlIlllIlllllIl = 'allure'
        if IlIIlIlllIllll.path.exists(IIIIIlIlllIlllllIl):
            lllllllllllllIl('Allure already exists. Skipping download.')
        else:
            lllllllllllllIl('Downloading Allure...')
            lllllllllllllIl("If setting up the Allure path fails due to access permissions, please set it up manually. Go to Environment Variables, find the 'Path' variable, and add the Allure path up to the 'bin' directory. You can verify the setup by running allure --version in the command prompt")
            urllib.request.urlretrieve(IlIlIIIIllIIIlIlII, IllIllllllllllIIll)
            lllllllllllllIl('Extracting Allure...')
            with IlIllIIlIlIlIl.ZipFile(IllIllllllllllIIll, 'r') as IIIlIllllIlIIlIIlI:
                IIIlIllllIlIIlIIlI.extractall(IIIIIlIlllIlllllIl)
            llIIlIIlIIlllIIIIl = IlIIlIlllIllll.environ.get('ProgramFiles', 'C:\\Program Files')
            IlllIlIIIllIllllll = IlIIlIlllIllll.path.join(llIIlIIlIIlllIIIIl, 'allure')
            if IlIIlIlllIllll.path.exists(IlllIlIIIllIllllll):
                llllllIIlIIlIl.rmtree(IlllIlIIIllIllllll)
            llllllIIlIIlIl.move(IIIIIlIlllIlllllIl, IlllIlIIIllIllllll)
            IlIIlIlllIllll.environ['PATH'] += IlIIlIlllIllll.pathsep + IlIIlIlllIllll.path.join(IlllIlIIIllIllllll, 'bin')
            lllllllllllllIl('Allure installed and PATH updated.')
        IlllllllIIlllIllll()
    except llllllllllllllI as llIllIIIllIIllIlIl:
        lllllllllllllIl(f'Error setting up Allure: {lllllllllllllII(llIllIIIllIIllIlIl)}')
        lllllllllllllIl("setting up the Allure path fails due to access permissions, please set it up manually. Go to Environment Variables, find the 'Path' variable, and add the Allure path up to the 'bin' directory. You can verify the setup by running allure --version in the command prompt")

def IIIIIIIIIIIIlllIlI():
    try:
        lIIIIlIIIlIIIIIlll = 'C:\\Program Files\\Java\\jdk-17'
        if IlIIlIlllIllll.path.exists(lIIIIlIIIlIIIIIlll):
            lllllllllllllIl('Java is already installed.')
        else:
            llIIlIIIlIlIllIlII = 'https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe'
            IllIIIIIllIIIlllII = 'jdk_installer.exe'
            lllllllllllllIl('Downloading Java...')
            urllib.request.urlretrieve(llIIlIIIlIlIllIlII, IllIIIIIllIIIlllII)
            lllllllllllllIl('Running Java installer...')
            IIlIlIIIIIIllIIlII(IllIIIIIllIIIlllII)
            IlIIlIlllIllll.environ['JAVA_HOME'] = lIIIIlIIIlIIIIIlll
            IlIIlIlllIllll.environ['PATH'] += IlIIlIlllIllll.pathsep + IlIIlIlllIllll.path.join(lIIIIlIIIlIIIIIlll, 'bin')
            lllllllllllllIl('Java installed and JAVA_HOME set.')
    except llllllllllllllI as llIllIIIllIIllIlIl:
        lllllllllllllIl(f'Error installing Java: {lllllllllllllII(llIllIIIllIIllIlIl)}')

def IIllIIlIIIIllllIIl():
    try:
        lllllIIIllIIlllIlI = 'elements'
        if not IlIIlIlllIllll.path.exists(lllllIIIllIIlllIlI):
            IlIIlIlllIllll.makedirs(lllllIIIllIIlllIlI)
            lllllllllllllIl(f'Created folder: {lllllIIIllIIlllIlI}')
        IllllIlIIlIIlllIll = IlIIlIlllIllll.path.join(lllllIIIllIIlllIlI, 'sample_element.py')
        if not IlIIlIlllIllll.path.exists(IllllIlIIlIIlllIll):
            with lllllllllllllll(IllllIlIIlIIlllIll, 'w') as IIlllllIIllIllllll:
                IIlllllIIllIllllll.write('# Add page elements here\n')
                IIlllllIIllIllllll.write('class elements:\n')
                IIlllllIIllIllllll.write('    google_search = "q"\n')
            lllllllllllllIl(f'Created sample file: {IllllIlIIlIIlllIll}')
        else:
            lllllllllllllIl(f'Sample file {IllllIlIIlIIlllIll} already exists.')
    except llllllllllllllI as llIllIIIllIIllIlIl:
        lllllllllllllIl(f'Error creating elements folder: {lllllllllllllII(llIllIIIllIIllIlIl)}')

def IllIlIlIIIlIIIIllI():
    try:
        lIIIIIlIIlIIllIlll = 'features'
        lIIllIIlllIIlIlIll = IlIIlIlllIllll.path.join(lIIIIIlIIlIIllIlll, 'steps')
        if not IlIIlIlllIllll.path.exists(lIIIIIlIIlIIllIlll):
            IlIIlIlllIllll.makedirs(lIIIIIlIIlIIllIlll)
            lllllllllllllIl(f'Created folder: {lIIIIIlIIlIIllIlll}')
        if not IlIIlIlllIllll.path.exists(lIIllIIlllIIlIlIll):
            IlIIlIlllIllll.makedirs(lIIllIIlllIIlIlIll)
            lllllllllllllIl(f'Created folder: {lIIllIIlllIIlIlIll}')
        IlIlIllIIIIlIlllIl = IlIIlIlllIllll.path.join(lIIIIIlIIlIIllIlll, 'search_google.feature')
        if not IlIIlIlllIllll.path.exists(IlIlIllIIIIlIlllIl):
            with lllllllllllllll(IlIlIllIIIIlIlllIl, 'w') as IIlllllIIllIllllll:
                IIlllllIIllIllllll.write('Feature: Search Google\n\n@smoke\nScenario: Search for kamran ghaffar on Google and click the first link\n    Given the user is on the Google homepage\n    When the user searches for kamran ghaffar\n    Then the user clicks on the first search result\n')
            lllllllllllllIl(f'Created feature file: {IlIlIllIIIIlIlllIl}')
        else:
            lllllllllllllIl(f'Feature file {IlIlIllIIIIlIlllIl} already exists.')
        lIlllllIlIIllIIIIl = IlIIlIlllIllll.path.join(lIIllIIlllIIlIlIll, 'search_google_steps.py')
        if not IlIIlIlllIllll.path.exists(lIlllllIlIIllIIIIl):
            with lllllllllllllll(lIlllllIlIIllIIIIl, 'w') as IIlllllIIllIllllll:
                IIlllllIIllIllllll.write('from behave import given, when, then\nfrom selenium.webdriver.common.by import By\nfrom selenium.webdriver.common.keys import Keys\nfrom elements.sample_element import elements\nfrom configuration import *\n\n@given(\'the user is on the Google homepage\')\ndef step_given_user_on_google_homepage(context):\n    context.driver.get(configuration_system.URL)\n\n@when(\'the user searches for kamran ghaffar\')\ndef step_when_user_searches(context):\n    search_box = context.driver.find_element(By.NAME, elements.google_search)\n    search_box.send_keys("kamran ghaffar" + Keys.RETURN)\n\n@then(\'the user clicks on the first search result\')\ndef step_then_click_first_result(context):\n    first_result = context.driver.find_element(By.CSS_SELECTOR, \'h3\')\n    first_result.click()\n')
            lllllllllllllIl(f'Created steps file: {lIlllllIlIIllIIIIl}')
        else:
            lllllllllllllIl(f'Steps file {lIlllllIlIIllIIIIl} already exists.')
        IIIlIIllllIllIlllI = IlIIlIlllIllll.path.join(lIIIIIlIIlIIllIlll, 'environment.py')
        if not IlIIlIlllIllll.path.exists(IIIlIIllllIllIlllI):
            with lllllllllllllll(IIIlIIllllIllIlllI, 'w') as IIlllllIIllIllllll:
                IIlllllIIllIllllll.write('from selenium import webdriver\nfrom selenium.webdriver.chrome.options import Options as ChromeOptions\nfrom selenium.webdriver.chrome.service import Service as ChromeService\nfrom selenium.webdriver.edge.options import Options as EdgeOptions\nfrom selenium.webdriver.edge.service import Service as EdgeService\nfrom selenium.webdriver.firefox.options import Options as FirefoxOptions\nfrom selenium.webdriver.firefox.service import Service as FirefoxService\nfrom webdriver_manager.chrome import ChromeDriverManager\nfrom webdriver_manager.firefox import GeckoDriverManager\nfrom webdriver_manager.microsoft import EdgeChromiumDriverManager\nfrom configuration import configuration_system\n\nfrom configuration import configuration_system\nfrom methods.utilities import *\n\n\ndef before_all(context):\n  pass\n\n\ndef before_feature(context, feature):\n    # Executed before each feature is run\n    pass\n\n\ndef before_scenario(context, scenario):\n    browser = context.config.userdata.get("browser", configuration_system.select_browser).lower()\n    headless = context.config.userdata.get("headless", configuration_system.headless_option).lower() == "true"\n\n    try:\n        if browser == "chrome":\n            chrome_options = ChromeOptions()\n            if headless:\n                chrome_options.add_argument("--headless")\n            chrome_options.add_argument("--disable-gpu")\n            chrome_options.add_argument("--window-size=1920,1200")\n            chrome_options.add_argument("--ignore-certificate-errors")\n\n            chrome_service = ChromeService(ChromeDriverManager().install())\n            context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)\n\n        elif browser == "firefox":\n            firefox_options = FirefoxOptions()\n            if headless:\n                firefox_options.add_argument("--headless")\n            firefox_options.add_argument("--window-size=1920,1200")\n            firefox_options.add_argument("--ignore-certificate-errors")\n\n            firefox_service = FirefoxService(GeckoDriverManager().install())\n            context.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)\n\n        elif browser == "edge":\n            edge_options = EdgeOptions()\n            if headless:\n                edge_options.add_argument("--headless")\n            edge_options.add_argument("--disable-gpu")\n            edge_options.add_argument("--window-size=1920,1200")\n            edge_options.add_argument("--ignore-certificate-errors")\n\n            edge_service = EdgeService(EdgeChromiumDriverManager().install())\n            context.driver = webdriver.Edge(service=edge_service, options=edge_options)\n\n        else:\n            raise ValueError(f"Unsupported browser: {browser}")\n\n        context.driver.maximize_window()\n        context.driver.implicitly_wait(30)\n\n    except Exception as e:\n        print(f"Error setting up the browser: {e}")\n        raise\n\n\ndef after_scenario(context, scenario):\n    # Close the browser after each scenario\n    context.driver.quit()\n\n\ndef after_step(context, step):\n    if configuration_system.screenshot:\n        step_capture_screenshot(context)\n\n\ndef after_feature(context, feature):\n    # Executed after each feature is run\n    pass\n\n\ndef after_all(context):\n    # Executed once after all scenarios are run\n    passed_scenarios = [scenario for scenario in context._runner.features if scenario.status.name == "passed"]\n    failed_scenarios = [scenario for scenario in context._runner.features if scenario.status.name == "failed"]\n    if configuration_system.report:\n        send_teams_webhook(passed_scenarios, failed_scenarios)\n\n')
            lllllllllllllIl(f'Created environment file: {IIIlIIllllIllIlllI}')
        else:
            lllllllllllllIl(f'Environment file {IIIlIIllllIllIlllI} already exists.')
    except llllllllllllllI as llIllIIIllIIllIlIl:
        lllllllllllllIl(f'Error creating features folder: {lllllllllllllII(llIllIIIllIIllIlIl)}')

def llllIllllllIllllll():
    try:
        IIIIIllllIIllIllII = 'methods'
        if not IlIIlIlllIllll.path.exists(IIIIIllllIIllIllII):
            IlIIlIlllIllll.makedirs(IIIIIllllIIllIllII)
            lllllllllllllIl(f'Created folder: {IIIIIllllIIllIllII}')
        llIIllIIIlIIllIIIl = IlIIlIlllIllll.path.join(IIIIIllllIIllIllII, 'utilities.py')
        if not IlIIlIlllIllll.path.exists(llIIllIIIlIIllIIIl):
            with lllllllllllllll(llIIllIIIlIIllIIIl, 'w') as IIlllllIIllIllllll:
                IIlllllIIllIllllll.write('import random\nimport os\nimport allure\nimport requests\nfrom selenium.common.exceptions import NoSuchElementException\nimport configuration\n\ndef step_capture_screenshot(context):\n    # Capture screenshot and save it in the "screenshots" directory\n    screenshot_dir = "screenshots"\n    os.makedirs(screenshot_dir, exist_ok=True)\n    random_3_digit_number = random.randint(100, 999)\n    ran_num = str(random_3_digit_number)\n    screenshot_name = "screenshot" + ran_num + ".png"\n    screenshot_path = os.path.join(screenshot_dir, screenshot_name)\n    context.driver.save_screenshot(screenshot_path)\n    # Attach the screenshot to the Allure report\n    with allure.step(\'Attach Screenshot\'):\n        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG, name=screenshot_name)\n\ndef trigger_webhook(total_failures, failure_details):\n    # Use the correct webhook URL from configuration\n    teams_webhook_url = configuration.configuration_system.webhook_url\n    payload = {\n        "@type": "MessageCard",\n        "@context": "",\n        "summary": "Test Automation Failure",\n        "title": "Failed Failed Failed!!!!",\n        "sections": [{\n            "activityTitle": "Test Automation Failure Details",\n            "activitySubtitle": f"Total Failures: {total_failures}",\n            "facts": [{\n                "name": "Total Failures",\n                "value": total_failures\n            }] + [\n                         {\n                             "name": f"Failure {i + 1}",\n                             "value": detail\n                         } for i, detail in enumerate(failure_details)\n                     ]\n        }]\n    }\n    try:\n        response = requests.post(teams_webhook_url, json=payload)\n        response.raise_for_status()  # Raise exception for HTTP errors\n    except Exception as e:\n        print("Error triggering webhook:", e)\n\ndef assert_element_exists(driver, by, locator, failure_details):\n    try:\n        driver.find_element(by, locator)\n    except NoSuchElementException:\n        failure_details.append(f"Element not found: {locator}")\n        total_failures = len(failure_details)\n        trigger_webhook(total_failures, failure_details)\n        raise AssertionError(f"Element not found: {locator}")\n\ndef send_teams_webhook(passed_scenarios, failed_scenarios):\n    # Teams webhook URL\n    webhook_url = configuration.configuration_system.webhook_url\n\n    # Format message for Teams\n    message = f"Total passed Features: {len(passed_scenarios)}"\n    message += f"Total failed Features: {len(failed_scenarios)}"\n    message += "Failed Features titles:"\n    for scenario in failed_scenarios:\n        message += f"- {scenario.name}"\n\n    # Payload for Microsoft Teams\n    payload = {\n        "@type": "MessageCard",\n        "@context": "Bee-links",\n        "summary": "Test Automation Report",\n        "title": "Notification From Software Quality Automation Team",\n        "text": message\n    }\n\n    # Send POST request to Teams webhook\n    response = requests.post(webhook_url, json=payload)\n\n    if response.status_code == 200:\n        print("Report sent to Teams Automation-Report channel successfully.")\n    else:\n        print(f"Failed to send message to Teams. Status code: {response.status_code}")\n')
            lllllllllllllIl(f'Created utilities file: {llIIllIIIlIIllIIIl}')
        else:
            lllllllllllllIl(f'Utilities file {llIIllIIIlIIllIIIl} already exists.')
    except llllllllllllllI as llIllIIIllIIllIlIl:
        lllllllllllllIl(f'Error creating methods folder: {lllllllllllllII(llIllIIIllIIllIlIl)}')

def llllIllIIllIlIlIlI():
    try:
        IIIIIIlIlIllIllIIl = 'configuration.py'
        if not IlIIlIlllIllll.path.exists(IIIIIIlIlIllIllIIl):
            with lllllllllllllll(IIIIIIlIlIllIllIIl, 'w') as IIlllllIIllIllllll:
                IIlllllIIllIllllll.write('class configuration_system:\n    webhook_url = "add webhook here"\n    screenshot = True\n    report = False\n    URL = "https://www.google.com"\n    select_browser = "edge"\n    headless_option = "false"\n    \n    \n')
            lllllllllllllIl(f'Created configuration file: {IIIIIIlIlIllIllIIl}')
        else:
            lllllllllllllIl(f'Configuration file {IIIIIIlIlIllIllIIl} already exists.')
    except llllllllllllllI as llIllIIIllIIllIlIl:
        lllllllllllllIl(f'Error creating configuration file: {lllllllllllllII(llIllIIIllIIllIlIl)}')

def IlllllllIIlllIllll():
    try:
        IlllllIlIllIIlIIll = 'import os\nimport subprocess\nfrom datetime import datetime\nimport http.server\nimport socketserver\nimport threading\nimport webbrowser\nimport time\nimport random\nimport string\n\ndef generate_random_string(length=10):\n    return \'\'.join(random.choices(string.ascii_letters, k=length))\n\nrandom_id = generate_random_string(3)\n\ndef run_tests_and_generate_report():\n    # Create a unique folder with today\'s date\n    today = datetime.now().strftime("%Y-%m-%d")\n    results_dir = f"allure_results_{today}_{random_id}"\n    report_dir = f"TestReport_{today}_{random_id}/allure_report"\n\n    # Create directories if they don\'t exist\n    os.makedirs(results_dir, exist_ok=True)\n    os.makedirs(report_dir, exist_ok=True)\n\n    # Define commands\n    behave_command = ["behave", "--tags=@smoke", "-f", "allure_behave.formatter:AllureFormatter", "-o", results_dir]\n    allure_generate_command = ["allure", "generate", results_dir, "-o", report_dir, "--clean"]\n\n    try:\n        # Run behave command to generate allure results\n        subprocess.run(behave_command, shell=True, check=True)\n    except subprocess.CalledProcessError as e:\n        print(f"Behave command failed with exit code {e.returncode}")\n\n    # Generate the allure report\n    subprocess.run(allure_generate_command, shell=True, check=True)\n\n    # Serve the generated report\n    serve_report(report_dir)\n\ndef serve_report(report_dir):\n    # Define the handler to serve files from the report directory\n    handler = http.server.SimpleHTTPRequestHandler\n    os.chdir(report_dir)\n\n    # Define the server\n    PORT = 8000\n    httpd = socketserver.TCPServer(("", PORT), handler)\n\n    # Open the report in the default web browser\n    webbrowser.open(f"http://localhost:{PORT}/index.html")\n\n    # Start the server\n    server_thread = threading.Thread(target=httpd.serve_forever)\n    server_thread.start()\n\n    # Allow some time for the browser to load the report\n    time.sleep(20)\n\n    # Shutdown the server\n    httpd.shutdown()\n    server_thread.join()\n\nif __name__ == "__main__":\n    run_tests_and_generate_report()\n'
        with lllllllllllllll('run-testcases.py', 'w') as IIlllllIIllIllllll:
            IIlllllIIllIllllll.write(IlllllIlIllIIlIIll)
        lllllllllllllIl('Created run-testcases.py script.')
    except llllllllllllllI as llIllIIIllIIllIlIl:
        lllllllllllllIl(f'Error creating run-testcases.py script: {lllllllllllllII(llIllIIIllIIllIlIl)}')
IIllllllIllIlllIlI()
IIIIIIIllIIIlIllIl()
IllIIllllIlllIIlll()
IIlllIlIlIlIIlIllI()
IIIIIIIIIIIIlllIlI()
IIllIIlIIIIllllIIl()
IllIlIlIIIlIIIIllI()
llllIllllllIllllll()
llllIllIIllIlIlIlI()
IlllllllIIlllIllll()
