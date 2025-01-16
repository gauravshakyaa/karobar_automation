import logging
import time
from pageObjects.InventoryPage import InventoryPage
from pageObjects.Party import Party
from selenium.webdriver.chrome.webdriver import WebDriver
from testCases import conftest
from utils import excel_utils
from selenium.webdriver.common.by import By

class Test_end_to_end:
    def test_end_to_end(self, setup, nav_to_dashboard):
        logging.info("Running End to End Test")
        driver : WebDriver = setup

        party = Party(driver)
        item = InventoryPage(driver)

        party_map_data = excel_utils.party_key_mapping
        item_map_data = excel_utils.item_key_mapping
        welcome_text_locator = (By.XPATH, "//*[contains(text(), 'Welcome')]")
        conftest.waitForElement(driver, locator=welcome_text_locator, timeout=3)
        
        # party_details = excel_utils.read_excel(filepath="utils//GuidedKarobarData.xlsx", sheetname="Party Data")
        # mapped_party_data = [excel_utils.map_excel_keys(data=party, key_mapping=party_map_data) for party in party_details]
        # for i, party_data in enumerate(mapped_party_data):
        #     party.addParty(**party_data)
        #     if i < len(mapped_party_data) - 1:
        #         party.clickSaveAddNewButton()
        #     else:
        #         party.clickSaveButton()
        
        
        item_details = excel_utils.read_excel(filepath="utils//GuidedKarobarData.xlsx", sheetname="Item Data")
        mapped_item_data = [excel_utils.map_excel_keys(data=item, key_mapping=item_map_data) for item in item_details]
        for i, item_data in enumerate(mapped_item_data):
            item.addItem(**item_data)
            if i < len(mapped_item_data) - 1:
                item.clickSaveAddNewButton()
            else:
                item.clickSaveButton()

        time.sleep(4)