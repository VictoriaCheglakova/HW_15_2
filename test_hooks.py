import allure
import pytest


@pytest.fixture()
def browser(request: pytest.FixtureRequest):
    pass


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if 'browser' in metafunc.fixturenames:
        if metafunc.config.getoption("--browser") == "all":
            pass
        else:
            pass


def test_desktop_page(browser):
    assert False


def test_mobile_page(browser):
    pass
