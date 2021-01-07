
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(request, browser):
    global driver
    if browser == 'Chrome':
        driver = webdriver.Chrome()

    elif browser == 'ff':
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)

    # if request.cls is not None:
    #     request.cls.driver = driver

    yield driver
    driver.quit()
