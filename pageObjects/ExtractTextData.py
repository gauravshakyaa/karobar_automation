import logging
from selenium.webdriver.common.by import By
from utils.readProperties import ReadConfig
from testCases import conftest
from selenium.webdriver.remote.webdriver import WebDriver

class ExtractTextData:
    text_toReceiveAmount_xpath = (By.XPATH, "//h2[normalize-space()='To Receive']//following-sibling::p")
    text_toGiveAmount_xpath = (By.XPATH, "//h2[normalize-space()='To Give']//following-sibling::p")
    text_salesAmount_xpath = (By.XPATH, "//h2[contains(., 'Sales')]//following-sibling::p")
    text_purchaseAmount_xpath = (By.XPATH, "//h2[contains(., 'Purchase')]//following-sibling::p")
    text_expenseAmount_xpath = (By.XPATH, "//h2[contains(., 'Expense')]//following-sibling::p")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.current_url = ReadConfig.getURL()
    
    def navigate_to_dashboard_page(self) -> None:
        if self.driver.current_url != self.current_url:
            self.driver.get(ReadConfig.getURL())
        else:
            logging.info("Already on Dashboard Page")
    
    def get_to_receive_amount_from_dashboard(self):
        self.navigate_to_dashboard_page()
        amount_with_currency_and_comma =  conftest.getTextFromTextField(self.driver, self.text_toReceiveAmount_xpath)
        return amount_with_currency_and_comma.strip("Rs. ").replace(",", "")
    
    def get_to_give_amount_from_dashboard(self):
        self.navigate_to_dashboard_page()
        amount_with_currency_and_comma =  conftest.getTextFromTextField(self.driver, self.text_toGiveAmount_xpath)
        return amount_with_currency_and_comma.strip("Rs. ").replace(",", "")

    def get_sales_amount_from_dashboard(self):
        self.navigate_to_dashboard_page()
        amount_with_currency_and_comma =  conftest.getTextFromTextField(self.driver, self.text_salesAmount_xpath)
        return amount_with_currency_and_comma.strip("Rs. ").replace(",", "")

    def get_purchase_amount_from_dashboard(self):
        self.navigate_to_dashboard_page()
        amount_with_currency_and_comma =  conftest.getTextFromTextField(self.driver, self.text_purchaseAmount_xpath)
        return amount_with_currency_and_comma.strip("Rs. ").replace(",", "")

    def get_expense_amount_from_dashboard(self):
        self.navigate_to_dashboard_page()
        amount_with_currency_and_comma =  conftest.getTextFromTextField(self.driver, self.text_expenseAmount_xpath)
        return amount_with_currency_and_comma.strip("Rs. ").replace(",", "")
    
    