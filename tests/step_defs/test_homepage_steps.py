from pytest_bdd import scenario, given, when, then


@scenario('../features/homepage.feature', 'Navigate to home page')
def test_add():
    pass


@given('homepage is displayed')
def home_page():
    pass


@when('the user clicks homepage')
def click_homepage():
    pass


@then('homepage page opens')
def home_page_opens():
    pass

