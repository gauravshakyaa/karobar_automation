import logging
import time
from pageObjects.Party import Party
from selenium.webdriver.chrome.webdriver import WebDriver
from testCases import conftest
from utilities import excel_utils
# from seleniumwire import webdriver as wire_webdriver

class Test_end_to_end:
    def test_end_to_end(self, setup, nav_to_dashboard):
        logging.info("Running End to End Test")
        driver : WebDriver = setup
        party = Party(driver)
        logging.info(driver.get_cookies())
        conftest.waitForElement(driver, "//*[contains(text(), 'Welcome')]")
        party_details = excel_utils.read_party_excel("utilities//GuidedKarobarData.xlsx")
        for index, party_data in enumerate(party_details):
            mapped_party_data = excel_utils.map_excel_keys(party_data)
            party.addParty(**mapped_party_data)
            if index < len(mapped_party_data) - 1:
                party.clickSaveAddNewButton()
            else:
                party.clickSaveButton()
