import allure
import pytest


def pytest_addoption(parser, pluginmanager):
    """Add browser and chrome-only options to pytest"""
    parser.addoption(
        "--browser",
        help="This is browser",
        required=False,
        default="chrome",
        choices=['chrome', 'firefox', 'all'],
    )
    parser.addoption(
        "--mobile-only",
        type=bool,
        default=False,
    )


def pytest_configure(config):
    """Skip tests for firefox if mobile-only option is True"""


def pytest_sessionstart(session):
    print("Session started!")


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_call(item):
    """Allure dynamic title"""
    yield


def pytest_collection_modifyitems(config, items: list[pytest.Item]):
    """
    Skip other tests if mobile-only option is True
    Sort tests if required
    """


def pytest_sessionfinish(session):
    pass


def pytest_report_teststatus(report, config):
    pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make screenshot"""
    outcome = yield
    result = outcome.get_result()
    # if item.when == "call" and result.failed is True:
    #     make_screenshot()
