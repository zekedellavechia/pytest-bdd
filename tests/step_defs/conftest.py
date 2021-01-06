import pytest
from selenium import webdriver
from pytest_bdd import scenarios


base_url = 'https://registry.qa.covid.gcp.rexdb.us/'

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def pytest_bdd_before_scenario():
    driver.maximize_window()


# def pytest_bdd_after_scenario():
#    driver.quit()


# Ezequiel Dellavechia 2020
