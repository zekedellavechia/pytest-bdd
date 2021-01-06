from selenium import webdriver
from tests.conftest import *


# Home Page
home_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us"]'
home_page_title = "h1[class='hero-title xl']"

about_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us/about"]'
about_page_title = 'h2.title'

results_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us/results"]'
results_page_title = 'a[href="https://registry.qa.covid.gcp.rexdb.us/reports"]'

