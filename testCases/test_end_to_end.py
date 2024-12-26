import logging
import time
from pageObjects.Party import Party
from selenium.webdriver.chrome.webdriver import WebDriver

from testCases import conftest
from utilities.readProperties import ReadConfig


class Test_end_to_end:
    logging.info("Running End to End Test")
    def test_end_to_end(self, setup, nav_to_dashboard):
        self.driver : WebDriver = setup
        party = Party(self.driver)
        conftest.waitForElement(self.driver, locator="//h2[contains(.,'Welcome')]")
        self.driver.get(f"{ReadConfig.getURL()}" + "/parties")
        party.clickAddNewPartyButton()
        time.sleep(3)
        party.setDate(day=1, month=1, year="2080")
        time.sleep(4)
        