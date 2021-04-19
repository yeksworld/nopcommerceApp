from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="C:/Users/yunus/AppData/Local/Drivers/chromedriver")
    return driver