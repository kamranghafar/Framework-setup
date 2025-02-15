import random
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
    message = f"Total passed Features: {len(passed_scenarios)}"
    message += f"Total failed Features: {len(failed_scenarios)}"
    message += "Failed Features titles:"
    for scenario in failed_scenarios:
        message += f"- {scenario.name}"

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
