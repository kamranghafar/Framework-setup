from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('the user is on the Google homepage')
def step_given_user_on_google_homepage(context):
    context.driver.get("https://www.google.com")

@when('the user searches for kamran ghaffar')
def step_when_user_searches(context):
    context.text.driver.get("https://www.google.com")

@then('the user clicks on the first search result')
def step_then_click_first_result(context):
    context.text.driver.get("https://www.google.com")
