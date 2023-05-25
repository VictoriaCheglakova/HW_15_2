import allure
import pytest


@pytest.fixture()
def browser(request: pytest.FixtureRequest):
    pass
    # request.config.getoption("--browser") == "chrome-98"
    # request.config.getoption("--browser") == "firefox"


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if 'browser' in metafunc.fixturenames:
        if metafunc.config.getoption("--browser") == "all":
            metafunc.parametrize("browser", ["chrome-98", "firefox"], indirect=True)
        else:
            metafunc.parametrize("browser", [metafunc.config.getoption("--browser")], indirect=True)


def test_desktop_page(browser, request):
    b = request.config.getoption("--browser")
    print()


def test_mobile_page(browser):
    pass
