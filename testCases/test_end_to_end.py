import logging
import time
import pytest
from pageObjects.Party import Party
from selenium.webdriver.chrome.webdriver import WebDriver
from testCases import conftest
from seleniumwire import webdriver as wire_webdriver

class Test_end_to_end:
    @pytest.mark.parametrize(
    "name, phone, balance, balanceType, address, email, pan",
        [
            ("Test Party 1", "9860725577", "1000", "To Receive", "Kathmandu", "test1@test.com", "123456789"),
        ]
    )
    def test_end_to_end(self, setup, nav_to_dashboard, name, phone, balance, balanceType, address, email, pan):
        logging.info("Running End to End Test")
        driver : WebDriver = setup
        party = Party(driver)
        driver_seleniumwire = wire_webdriver.Chrome()
        for request in driver_seleniumwire.requests:
            if request.response:
                logging.info(f"Request URL: {request.url}")
                logging.info(f"Request Method: {request.method}")
                logging.info(f"Request Response Code: {request.response.status_code}")
                logging.info(f"Request Response Body: {request.response.body}")
        logging.info(driver.get_cookies())
        conftest.waitForElement(driver, "//*[contains(text(), 'Welcome')]")
        party_details = {
            "name": name,
            "phone": phone,
            "balance": balance,
            "balanceType": balanceType,
            "address": address,
            "email": email,
            "pan": pan,
        }
        party.addParty(**party_details)
        party.clickSaveButton()
        time.sleep(2)
