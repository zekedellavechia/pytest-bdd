from pytest_bdd import scenarios, when, then, given
from tests.pages.homepage_page import *
from tests.conftest import *
from selenium import webdriver
from time import sleep


# Path for Scenarios

scenarios('../features/homepage.feature')


# Fixtures


# Steps


# Given
@given('homepage is displayed')
def home_page():
    driver.get(base_url)


# When
@when('the user clicks home')
def click_button():
    driver.find_element_by_css_selector(home_button).click()


@when('the user clicks results')
def click_results():
    driver.find_element_by_css_selector(results_button).click()


@when('the user clicks about')
def user_clicks_about():
    driver.find_element_by_css_selector(about_button).click()


@when('the user clicks contact us')
def user_clicks_contact_us():
    driver.find_element_by_css_selector(contact_us_button).click()


@when('the user clicks FAQ')
def user_clicks_faq():
    driver.find_element_by_css_selector(faq_button).click()


@when('the user clicks resources')
def user_clicks_resources():
    driver.find_element_by_css_selector(results_button).click()


@when('the user clicks our partners')
def user_clicks_our_partners():
    driver.find_element_by_css_selector(our_partners_button).click()


# Then
@then('resources page opens')
def resources_page_opens():
    driver.find_element_by_css_selector(resources_title).is_displayed()


@then('our partners page opens')
def our_partners_page_opens():
    driver.find_element_by_css_selector(our_partners_title).is_displayed()


@then('contact us page opens')
def contact_us_page_opens():
    driver.find_element_by_css_selector(contact_us_title).is_displayed()


@then('homepage page opens')
def home_page_opens():
    driver.find_element_by_css_selector(home_page_title).is_displayed()


@then('results page opens')
def home_page_opens():
    driver.find_element_by_css_selector(results_page_title).is_displayed()


@then('FAQ page opens')
def faq_page_opens():
    driver.find_element_by_css_selector(faq_title).is_displayed()


@then('about page opens')
def about_page_opens():
    driver.find_element_by_css_selector(about_page_title).is_displayed()


@then('close browser')
def close_browser():
    driver.close()



