"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser

@pytest.fixture(params=["mobile", "desktop"])
def window(request):
    if request.param == "mobile":
        browser.driver.set_window_size(640, 960)
    if request.param == "desktop":
        browser.driver.set_window_size(1920, 1080)

@pytest.mark.parametrize("window", ["desktop"], indirect=True)
def test_github_desktop(window):
    assert browser.element('.HeaderMenu-link HeaderMenu-button d-inline-flex d-lg-none flex-order-1 f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit js-prevent-focus-on-mobile-nav')

@pytest.mark.parametrize("window", ["mobile"], indirect=True)
def test_github_mobile(window):
    assert browser.element('.HeaderMenu-link HeaderMenu-button d-inline-flex d-lg-none flex-order-1 f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit js-prevent-focus-on-mobile-nav')