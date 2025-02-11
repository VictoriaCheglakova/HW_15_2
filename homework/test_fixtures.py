"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture()
def win_desktop():
    browser.driver().set_window_size(1920, 1080)
    browser.driver().set_window_size(1920, 1080)

@pytest.fixture()
def win_mobile():
    browser.driver().set_window_size(640, 960)



def test_github_desktop(win_desktop):
    browser.open_url('https://github.com/')
    #browser.open('https://github.com/')


def test_github_mobile(win_mobile):
    browser.open_url('https://github.com/')