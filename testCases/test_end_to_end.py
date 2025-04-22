import logging
import time

import pytest
from pageObjects.ExtractTextData import ExtractTextData
from pageObjects.PaymentInOutPage import PaymentInOut
from pageObjects.ManageAccount import ManageAccount
from pageObjects.TransactionPage import TransactionPage
from pageObjects.InventoryPage import InventoryPage
from pageObjects.IncomeExpensePage import IncomeExpense
from pageObjects.NavigateToPage import NavigateToPage
from pageObjects.PartyPage import Party
from selenium.webdriver.remote.webdriver import WebDriver
from testCases import conftest
from selenium.webdriver.common.by import By

class Test_end_to_end:
    @pytest.mark.skip()
    def test_end_to_end(self, setup, nav_to_dashboard):
        logging.info("Running End to End Test")
        driver : WebDriver = setup
        party = Party(driver)
        item = InventoryPage(driver)
        transaction = TransactionPage(driver)
        account = ManageAccount(driver)
        payments = PaymentInOut(driver)
        income_expense = IncomeExpense(driver)
        extract_txt_data = ExtractTextData(driver)
        welcome_text_locator = (By.XPATH, "//h2[contains(text(), 'Welcome')]")
        conftest.waitForElement(driver, locator=welcome_text_locator, timeout=10)
        item.addNewUnit()
        party.addBulkParty()
        assert extract_txt_data.get_to_receive_amount_from_dashboard() == "3032.12", "To Receive amount is not as expected after adding bulk parties"
        assert extract_txt_data.get_to_give_amount_from_dashboard() == "5553.48", "To Give amount is not as expected after adding bulk parties"
        logging.info("Bulk Parties added successfully")
        item.addBulkItems()
        logging.info("Bulk Items added successfully")
        item.addBulkItemAdjustments()
        logging.info("Bulk Item Adjustments added successfully")
        account.add_bulk_accounts()
        logging.info("Bulk Accounts added successfully")
        account.add_bulk_account_adjustments()
        logging.info("Bulk Account Adjustments added successfully")
        payments.add_bulk_payment_in_out(transaction_type="in")
        payments.add_bulk_payment_in_out(transaction_type="out")
        logging.info("Bulk Payment In/Out added successfully")
        transaction.addBulkTransactions(transaction_type="s")
        transaction.addBulkTransactions(transaction_type="sr")
        transaction.addBulkTransactions(transaction_type="p")
        transaction.addBulkTransactions(transaction_type="pr")
        transaction.addBulkTransactions(transaction_type="q")
        income_expense.add_bulk_income_expense(transaction_type="expense")
        income_expense.add_bulk_income_expense(transaction_type="income")
        time.sleep(1)
        logging.info("End to End Test Completed")
    
    # @pytest.mark.skip(reason="")
    def test_testing(self, setup, nav_to_dashboard):
        driver = setup
        extract_data = ExtractTextData(driver)
        party = Party(driver)
        income_expense = IncomeExpense(driver)
        income_expense.add_income_expense(transaction_type="expense", category="Utilities", number="1", total_amount="1000", payment_mode="Cash")
        time.sleep(2)
        income_expense.add_income_expense(transaction_type="expense", category="Utilities", number="2", total_amount="500", payment_mode="Cash")
        time.sleep(3)
        