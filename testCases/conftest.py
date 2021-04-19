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
    else:
        driver = webdriver.Ie(executable_path="C:/Users/yunus/AppData/Local/Drivers/msedgedriver")
        print("Launching Edge browser...........")

    return driver


def pytest_addoption(parser):  # This will get value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")

############# PyTest HTML Report ####################
# It is hook for Adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
