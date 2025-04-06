import logging
from utils.readProperties import ReadConfig
from selenium.webdriver.remote.webdriver import WebDriver
from testCases import conftest
from selenium.webdriver.common.by import By
class NavigateToPage:
    def __init__(self, driver):
        self.driver : WebDriver = driver
        self.base_url = ReadConfig.getURL()
        self.parties_list = self.base_url = "/parties"

        self.item_list = self.base_url + "/inventory"
        self.item_detail = self.base_url + "/inventory/item-detail"
        self.add_item = self.base_url + "/inventory/add"

        self.sales_list = self.base_url + "/sales-invoices"
        self.add_sales = self.base_url + "/sales-invoices/create"
        self.payment_in_list = self.base_url + "/payment-in"
        self.quotation_list = self.base_url + "/quotations"
        self.add_quotation = self.base_url + "/quotations/create"
        self.sales_return_list = self.base_url + "/sales-return"
        self.add_sales_return = self.base_url + "/sales-return/create"

        self.purchase_list = self.base_url + "/purchase"
        self.add_purchase = self.base_url + "/purchase/create"
        self.payment_out_list = self.base_url + "/payment-out"
        self.purchase_return_list = self.base_url + "/purchase-return"
        self.add_purchase_return = self.base_url + "/purchase-return/create"

        self.expenses_list = self.base_url + "/expense"
        self.income_list = self.base_url + "/income"
        
        self.accounts_list = self.base_url + "/manage-account"

        self.reports_list = self.base_url + "/reports"
        self.sales_report = self.base_url + "/reports/sales"
        self.purchase_report = self.base_url + "/reports/purchase"
        self.sales_return_report = self.base_url + "/reports/sales-return"
        self.purchase_return_report = self.base_url + "/reports/purchase-return"
        self.data_book_report = self.base_url + "/reports/day-book"
        self.all_transactions_report = self.base_url + "/reports/all-transactions"
        self.profit_loss_report = self.base_url + "/reports/profit-and-loss"
        self.party_statement_report = self.base_url + "/reports/party-statement"
        self.all_parties_report = self.base_url + "/reports/all-party"
        self.item_details_report = self.base_url + "/reports/item-detail"
        self.item_rate_report = self.base_url + "/reports/item-rate-list"
        self.low_Stock_report = self.base_url + "/reports/low-stock-summary"
        self.stock_qty_report = self.base_url + "/reports/stock-quantity"

    def already_on_page(self, page_url):
        return self.driver.current_url == page_url
    
    def wait_until_text_visible(self, text, timeout=3):
        locator = (By.XPATH, f"//h2[normalize-space()='{text}']")
        conftest.waitForElement(self.driver, text, locator=locator, timeout=timeout, condition="visible")

    def navigate_to_dashboard(self):
        if self.already_on_page(self.base_url):
            logging.info("Already on Dashboard, continuing...")
        else:
            logging.info("Navigating to Dashboard...")
            self.driver.get(self.base_url)

    def navigate_to_parties(self):
        if self.already_on_page(self.parties_list):
            logging.info("Already on Parties List, continuing...")
        else:
            logging.info("Navigating to Parties List...")
            self.driver.get(self.parties_list)
            conftest.waitForElement(self.driver)

    def navigate_to_item_list(self):
        if self.already_on_page(self.item_list):
            logging.info("Already on Item List, continuing...")
