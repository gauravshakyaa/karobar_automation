from pageObjects.Party import Party
from selenium.webdriver.chrome.webdriver import WebDriver

from utilities.readProperties import ReadConfig


class Test_end_to_end:
    def test_end_to_end(self, setup, nav_to_dashboard):
        self.driver : WebDriver = setup
        party = Party(self.driver)
        self.driver.get(ReadConfig.getBrowser + "/party")
        party.clickAddNewPartyButton()