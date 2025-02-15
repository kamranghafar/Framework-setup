from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from configuration import configuration_system

from configuration import configuration_system
from methods.utilities import *


def before_all(context):
  pass


def before_feature(context, feature):
    # Executed before each feature is run
    pass


def before_scenario(context, scenario):
    browser = context.config.userdata.get("browser", configuration_system.select_browser).lower()
    headless = context.config.userdata.get("headless", configuration_system.headless_option).lower() == "False"

    try:
        if browser == "chrome":
            chrome_options = ChromeOptions()
            if headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1200")
            chrome_options.add_argument("--ignore-certificate-errors")

            chrome_service = ChromeService(ChromeDriverManager().install())
            context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        elif browser == "firefox":
            firefox_options = FirefoxOptions()
            if headless:
                firefox_options.add_argument("--headless")
            firefox_options.add_argument("--window-size=1920,1200")
            firefox_options.add_argument("--ignore-certificate-errors")

            firefox_service = FirefoxService(GeckoDriverManager().install())
            context.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

        elif browser == "edge":
            edge_options = EdgeOptions()
            if headless:
                edge_options.add_argument("--headless")
            edge_options.add_argument("--disable-gpu")
            edge_options.add_argument("--window-size=1920,1200")
            edge_options.add_argument("--ignore-certificate-errors")

            edge_service = EdgeService(EdgeChromiumDriverManager().install())
            context.driver = webdriver.Edge(service=edge_service, options=edge_options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        context.driver.maximize_window()
        context.driver.implicitly_wait(30)

    except Exception as e:
        print(f"Error setting up the browser: {e}")
        raise


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
