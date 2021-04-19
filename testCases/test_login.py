import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL
    username = ReadConfig.getUseremail
    password = ReadConfig.getPassword

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************** Test_001_Login **************")
        self.logger.info("*********** Verifiying Home Page Title ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login23":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Home page title test is failed ***********")
            assert False

    def test_login(self,setup):
        self.logger.info("***************** Verifying Login test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration23":
            assert True
            self.logger.info("****************** Login test is passed **************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****************** Login test is failed **************")
            assert False
