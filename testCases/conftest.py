from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/yunus/AppData/Local/Drivers/chromedriver")
        print("Launching Chrome browser...........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/yunus/AppData/Local/Drivers/geckodriver")
        print("Launching Firefox browser...........")


    return driver


def pytest_addoption(parser):  # This will get value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")
