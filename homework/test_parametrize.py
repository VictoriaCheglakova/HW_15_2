"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser as window

@pytest.fixture(params=["mobile", "desktop"])
def browser(request):
    if request.param == "mobile":
        return window.driver().set_window_size(640, 960)
    if request.param == "desktop":
        return window.driver().set_window_size(1920, 1080)

@pytest.mark.parametrize("browser", ["desktop"], indirect=True)
def test_github_desktop(browser):
    window.open_url('https://github.com/')

@pytest.mark.parametrize("browser", ["mobile"], indirect=True)
def test_github_mobile(browser):
    window.open_url('https://github.com/')