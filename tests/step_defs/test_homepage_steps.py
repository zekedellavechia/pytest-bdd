from pytest_bdd import scenarios, given, when, then
from selene.api import s
from tests.step_defs.conftest import *

# Path for Scenarios
scenarios('../features/homepage.feature')


@given('homepage is displayed')
def home_page():
    browser.open_url(base_url)


@when('the user clicks home')
def click_button():
    s('a[href="https://registry.qa.covid.gcp.rexdb.us"]').click()


@when('the user clicks results')
def click_homepage():
    s('a[href="https://registry.qa.covid.gcp.rexdb.us/results"]').click()


@then('homepage page opens')
def home_page_opens():
    s('h1[class="hero-title xl"]').is_displayed()


@then('results page opens')
def home_page_opens():
    s('h2[class="page-title"]').is_displayed()


@then('close browser')
def close_browser():
    browser.close()


@when('the user clicks about')
def user_clicks_about():
    s('a[href="https://registry.qa.covid.gcp.rexdb.us/about"]').click()


@then('about page opens')
def about_page_opens():
    pass
