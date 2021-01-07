import pytest
from selenium import webdriver
from pytest_bdd import scenarios

base_url = 'https://registry.qa.covid.gcp.rexdb.us/'


browser = webdriver.Chrome()
browser.implicitly_wait(10)


def pytest_bdd_before_scenario():
    browser.maximize_window()


# def pytest_bdd_after_scenario():
#    browser.quit()

