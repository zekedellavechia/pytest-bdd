from pytest_bdd import scenarios, given, when, then
from selene.api import s
from tests.step_defs.conftest import *
from tests.locators import *

# Path for Scenarios
scenarios('../features/homepage.feature')


@given('homepage is displayed')
def home_page():
    browser.open_url(base_url)


@when('the user clicks home')
def click_button():
    s(home_button).click()


@when('the user clicks results')
def click_results():
    s(results_button).click()


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


@when('the user clicks FAQ')
def user_clicks_faq():
    s('a[href="https://registry.qa.covid.gcp.rexdb.us/faq"]').click()


@then('FAQ page opens')
def faq_page_opens():
    pass


@when('the user clicks resources')
def user_clicks_resources():
    s('a[href="https://registry.qa.covid.gcp.rexdb.us/resources"]').click()


@then('resources page opens')
def resources_page_opens():
    pass


@when('the user clicks our partners')
def user_clicks_our_partners():
    s('a[href="https://registry.qa.covid.gcp.rexdb.us/partners"]').click()


@then('our partners page opens')
def our_partners_page_opens():
    pass


@when('the user clicks contact us')
def user_clicks_contact_us():
    s('a[href="https://registry.qa.covid.gcp.rexdb.us/contacts"]').click()


@then('contact us page opens')
def contact_us_page_opens():
    pass