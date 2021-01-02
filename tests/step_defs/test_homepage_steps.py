from pytest_bdd import scenarios, given, when, then, parsers
from conftest import *

# SCENARIOS
scenarios('../features/homepage.feature')


# STEPS


@given('homepage is displayed')
def home_page():
    driver.get(base_url)


@when('the user clicks home')
def click_button():
    driver.find_element_by_css_selector('a[href="https://registry.qa.covid.gcp.rexdb.us"]').click()


@when('the user clicks results')
def click_homepage():
    driver.find_element_by_css_selector('a[href="https://registry.qa.covid.gcp.rexdb.us/results"]').click()


@then('homepage page opens')
def home_page_opens():
    driver.find_element_by_css_selector('h1[class="hero-title xl"]').is_displayed()


@then('results page opens')
def home_page_opens():
    driver.find_element_by_css_selector('h2[class="page-title"]').is_displayed()


@then('close browser')
def close_browser():
    driver.close()
