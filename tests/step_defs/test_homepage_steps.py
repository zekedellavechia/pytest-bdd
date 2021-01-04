from pytest_bdd import scenarios, given, when, then
from tests.pages.homepage_page import *
from conftest import *
from selene import browser


# Path for Scenarios

scenarios('../features/homepage.feature')


# Fixtures


# Steps


# Given
@given('homepage is displayed')
def home_page():
    browser.open_url(base_url)


# When
@when('the user clicks home')
def click_button():
    home_button.click()


@when('the user clicks results')
def click_results():
    results_button.click()


@when('the user clicks about')
def user_clicks_about():
    about_button.click()


@when('the user clicks contact us')
def user_clicks_contact_us():
    contact_us_button.click()


@when('the user clicks FAQ')
def user_clicks_faq():
    faq_button.click()


@when('the user clicks resources')
def user_clicks_resources():
    resources_button.click()


# Then
@then('resources page opens')
def resources_page_opens():
    pass


@when('the user clicks our partners')
def user_clicks_our_partners():
    our_partners_button.click()


@then('our partners page opens')
def our_partners_page_opens():
    pass


@then('contact us page opens')
def contact_us_page_opens():
    pass


@then('homepage page opens')
def home_page_opens():
    home_page_title.is_displayed()


@then('results page opens')
def home_page_opens():
    results_page_title.is_displayed()


@then('close browser')
def close_browser():
    browser.close()


@then('FAQ page opens')
def faq_page_opens():
    pass


@then('about page opens')
def about_page_opens():
    pass
