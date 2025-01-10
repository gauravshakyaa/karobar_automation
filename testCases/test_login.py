import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import logging
from pageObjects.LoginPage import LoginPage
# from utilities.customLogger import LogGenerator
from utils.readProperties import ReadConfig
from testCases import conftest
from selenium.webdriver.chrome.webdriver import WebDriver
import allure
from allure_commons.types import AttachmentType
from utils.customLogger import setup_logging

class Test_001_Login:
    setup_logging()
    num = ReadConfig.getPhoneNumber()
    # @pytest.mark.parametrize(
    #         "phone_number", [
    #             "9", "9860", "986072557", ""
    #         ]
    # )
    @allure.step("Running test_inputEmptyPhoneNumber")
    @allure.severity(allure.severity_level.MINOR)
    @allure.feature("Test phone number validation passing different inputs.")
    @allure.story("Login page Test")
    def test_inputEmptyPhoneNumber(self, setup):
        logging.info("this is")
        inputs = ["9", "9860", "986072557", ""]
        self.driver: WebDriver = setup
        loginpage = LoginPage(self.driver)
        time.sleep(1)
        for input in inputs:
            loginpage.setPhoneNumber(input)
            time.sleep(1)
            loginpage.clickContinueButton()
            time.sleep(1)
            text = loginpage.returnPhoneTextFieldErrorMessage()
            if text == 'Invalid phone number format':
                self.logger.info(f"Passed for input: {input}")
            else:
                allure.attach(self.driver.get_screenshot_as_png(), 
                              name=f"Failed_Input_{input}", 
                              attachment_type=AttachmentType.PNG)
                self.logger.critical("Failed in test_inputEmptyPhoneNumber")
                self.driver.close()
                assert False, f"Failed for input: {input}"
        self.driver.close()
        assert True, "test_inputEmptyPhoneNumber, All inputs passed successfully."
    