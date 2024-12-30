import logging
import time
from pageObjects. import Party
from selenium.webdriver.chrome.webdriver import WebDriver
from testCases import conftest


class Test_end_to_end:
    def test_end_to_end(self, setup, nav_to_dashboard):
        logging.info("Running End to End Test")
        self.driver : WebDriver = setup
        party = Party(self.driver)
        conftest.waitForElement(self.driver, "//*[contains(text(), 'Welcome')]")
        # party.addParty(name="Test Party", phone="9860725577", balance="1000", 
        #                balanceType="To Receive", address="Kathmandu", 
        #                email="test@test.com", pan="123456789")
        party.addParty(name="Test Party")
        party.clickSaveButton()
        time.sleep(5)
