import pytest
from pytest_bdd import given
from selenium import webdriver

driver = webdriver.Chrome()


base_url = 'https://registry.qa.covid.gcp.rexdb.us/'


def pytest_bdd_after_scenario():
    driver.close()


# Ezequiel Dellavechia 2020
