from selene.api import s
from selenium import webdriver
from tests.conftest import *


# Home Page
home_button = s('a[href="https://registry.qa.covid.gcp.rexdb.us"]')
results_button = s('a[href="https://registry.qa.covid.gcp.rexdb.us/results"]')
home_page_title = s('h1[class="hero-title xl"]')
results_page_title = s('h2[class="page-title"]')
about_button = s('a[href="https://registry.qa.covid.gcp.rexdb.us/about"]')
faq_button = s('a[href="https://registry.qa.covid.gcp.rexdb.us/faq"]')
resources_button = s('a[href="https://registry.qa.covid.gcp.rexdb.us/resources"]')
our_partners_button = s('a[href="https://registry.qa.covid.gcp.rexdb.us/partners"]')
contact_us_button = s('a[href="https://registry.qa.covid.gcp.rexdb.us/contacts"]')
