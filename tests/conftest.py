import pytest
from selenium import webdriver

base_url = 'https://registry.qa.covid.gcp.rexdb.us/'

driver = webdriver.Chrome()


def pytest_bdd_before_scenario():
    driver.maximize_window()


# def pytest_bdd_after_scenario():
#    driver.close()


# Ezequiel Dellavechia 2020
