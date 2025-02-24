import logging
import time
from pageObjects.TransactionPage import TransactionPage
from pageObjects.InventoryPage import InventoryPage
from pageObjects.Party import Party
from selenium.webdriver.remote.webdriver import WebDriver
from testCases import conftest
from utils import excel_utils
from selenium.webdriver.common.by import By

class Test_end_to_end:
    def test_end_to_end(self, setup, nav_to_dashboard):
        logging.info("Running End to End Test")
        driver : WebDriver = setup
        party = Party(driver)
        item = InventoryPage(driver)
        transaction = TransactionPage(driver)

        welcome_text_locator = (By.XPATH, "//*[contains(text(), 'Welcome')]")
        conftest.waitForElement(driver, locator=welcome_text_locator, timeout=3)

        # party.addBulkParty()
        # item.addBulkItems()
        # transaction.addTransaction(transaction_type="s", party_name="Party 1", items=[{"item_name":"Item 3", "quantity":"10", "secondary_unit":"PCS", "rate":"100", "item_discount_percent":"10"}, {"item_name":"Item 2", "quantity":"2", "rate":"2", "item_discount_percent":"10"}], overall_discount_percent="10", tax=True, charge_amount=[100, 500])

        transaction.addBulkTransactions(transaction_type="s")
        # transaction.addBulkTransactions(transaction_type="p")
        # transaction.addBulkTransactions(transaction_type="sr")
        # transaction.addBulkTransactions(transaction_type="pr")
        # transaction.addBulkTransactions(transaction_type="q")
        
        time.sleep(5)
        