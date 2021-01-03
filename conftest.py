from selenium import webdriver
from selene import config, browser


driver = webdriver.Chrome()
config.timeout = 3
browser.set_driver(driver)
base_url = 'https://registry.qa.covid.gcp.rexdb.us/'
driver.maximize_window()


# Ezequiel Dellavechia 2020
