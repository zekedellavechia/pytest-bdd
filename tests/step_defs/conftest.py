from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
base_url = 'https://registry.qa.covid.gcp.rexdb.us/'
