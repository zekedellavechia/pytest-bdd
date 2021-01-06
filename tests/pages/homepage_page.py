from selenium import webdriver
from tests.conftest import *


# Home Page
home_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us"]'
home_page_title = "h1[class='hero-title xl']"

about_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us/about"]'
about_page_title = 'h2.title'

results_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us/results"]'
results_page_title = 'a[href="https://registry.qa.covid.gcp.rexdb.us/reports"]'

faq_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us/faq"]'
faq_title = 'h2[class="page-title mb-20"]'

resources_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us/resources"]'
resources_title = 'h2[class="page-title"]'

our_partners_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us/partners"]'
our_partners_title = 'h2[class="page-title"]'


contact_us_button = 'a[href="https://registry.qa.covid.gcp.rexdb.us/contacts"]'
contact_us_title = 'h2[class="title"]'

