from pytest_bdd import given, when, then
from tests.conftest import *

scenarios('../features/login.feature', '../features/homepage.feature', )


@given("login page is displayed")
def click_login_button():
    browser.get(base_url)
    browser.find_element_by_css_selector('a[class="cta cta-transparent"]').click()


@when("the user enters valid credentials")
def step_impl():
    pass


@then("the user accesses the site")
def step_impl():
    pass