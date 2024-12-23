import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pageObjects.LoginPage import LoginPage
# from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadConfig
from testCases import conftest
from selenium.webdriver.chrome.webdriver import WebDriver
import allure
from allure_commons.types import AttachmentType

class Test_001_Sales:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sales(self, setup):
        self.driver: WebDriver = setup
        loginpage = LoginPage(self.driver)
        time.sleep(1)
        loginpage.clickContinueButton()
        time.sleep(1)
        text = loginpage.returnPhoneTextFieldErrorMessage()
        if text == 'Invalid phone number format':
            assert True
            self.driver.close()
            
        else:
            allure.attach(self.driver.get_screenshot_as_png, name="testLoginScreen", attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False