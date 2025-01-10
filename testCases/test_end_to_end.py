import logging
import time
from pageObjects.Party import Party
from selenium.webdriver.chrome.webdriver import WebDriver
from testCases import conftest
from utils import excel_utils

class Test_end_to_end:
    def test_end_to_end(self, setup, nav_to_dashboard):
        logging.info("Running End to End Test")
        driver : WebDriver = setup
        party = Party(driver)
        conftest.waitForElement(driver, "//*[contains(text(), 'Welcome')]")
        party_details = excel_utils.read_party_excel("utils//GuidedKarobarData.xlsx")
        for index, party_data in enumerate(party_details):
            mapped_party_data = excel_utils.map_excel_keys(party_data)
            party.addParty(**mapped_party_data)
            party.clickSaveAddNewButton()
            time.sleep(1)