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
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--remote-debugging-port=9222")  # Prevents the DevToolsActivePort error
    edge_options.add_argument("--headless=new")  # Run tests in headless mode to avoid UI crashes
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")

    edge_service = EdgeService(EdgeChromiumDriverManager().install())
    context.driver = webdriver.Edge(service=edge_service, options=edge_options)

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
