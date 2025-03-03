import logging
import time
from pageObjects.ManageAccount import ManageAccount
from pageObjects.TransactionPage import TransactionPage
from pageObjects.InventoryPage import InventoryPage
from pageObjects.Party import Party
from selenium.webdriver.remote.webdriver import WebDriver
from testCases import conftest
from utils import excel_utils
from selenium.webdriver.common.by import By

from utils.readProperties import ReadConfig

class Test_end_to_end:
    def test_end_to_end(self, setup, nav_to_dashboard):
        logging.info("Running End to End Test")
        driver : WebDriver = setup
        party = Party(driver)
        item = InventoryPage(driver)
        transaction = TransactionPage(driver)
        account = ManageAccount(driver)
        welcome_text_locator = (By.XPATH, "//*[contains(text(), 'Welcome')]")
        conftest.waitForElement(driver, locator=welcome_text_locator, timeout=3)

        # party.addBulkParty()
        # item.addBulkItems()
        # item.addBulkItemAdjustments()
        # account.add_bulk_accounts()
        transaction.addBulkTransactions(transaction_type="s")
        time.sleep(5)
        