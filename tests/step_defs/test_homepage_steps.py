from pytest_bdd import scenario, given, when, then
from conftest import *


# SCENARIOS


@scenario('../features/homepage.feature', 'Navigate to home page')
def test_navigate_to_home_page():
    pass


@scenario('../features/homepage.feature', 'Navigate to results page')
def test_navigate_to_results_page():
    pass


# STEPS


@given('homepage is displayed')
def home_page():
    driver.get(base_url)


@when('the user clicks homepage')
def click_homepage():
    pass


@when('the user clicks results')
def click_homepage():
    pass


@then('homepage page opens')
def home_page_opens():
    pass


@then('results page opens')
def home_page_opens():
    pass
