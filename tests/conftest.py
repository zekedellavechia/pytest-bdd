import pytest
from pytest_bdd import given
from selenium import webdriver
from selene import browser



base_url = 'https://registry.qa.covid.gcp.rexdb.us/'


def pytest_bdd_after_scenario():
    browser.close()






# Discards


# chromedriver_path = ChromeDriverManager().install()

# def setup():
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument('--window-size=1920x1080')
# driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
# driver.maximize_window()
# config.timeout = 10
# browser.set_driver(driver)


# Ezequiel Dellavechia 2020
