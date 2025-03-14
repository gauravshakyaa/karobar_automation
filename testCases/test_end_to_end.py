import logging
import time

import pytest
from pageObjects.PaymentInOut import PaymentInOut
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
        payments = PaymentInOut(driver)
        welcome_text_locator = (By.XPATH, "//h2[contains(text(), 'Welcome')]")
        conftest.waitForElement(driver, locator=welcome_text_locator, timeout=10)
        # party.addBulkParty()
        # item.addBulkItems()
        # item.addBulkItemAdjustments()
        # account.add_bulk_accounts()
        # account.add_bulk_account_adjustments()
        # payments.add_bulk_payment_in_out(transaction_type="in")
        # payments.add_bulk_payment_in_out(transaction_type="out")
        # transaction.addBulkTransactions(transaction_type="s")
        # transaction.addBulkTransactions(transaction_type="sr")
        # transaction.addBulkTransactions(transaction_type="p")
        # transaction.addBulkTransactions(transaction_type="pr")
        # transaction.addBulkTransactions(transaction_type="q")
        
        time.sleep(5)
        
