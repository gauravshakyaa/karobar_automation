import logging
from selenium.webdriver.common.by import By
from testCases import conftest
from selenium.webdriver.remote.webdriver import WebDriver
from pageObjects.NavigateToPage import NavigateToPage

class ExtractTextData(NavigateToPage):
    text_toReceiveAmount_xpath = (By.XPATH, "//h2[normalize-space()='To Receive']//following-sibling::p")
    text_toGiveAmount_xpath = (By.XPATH, "//h2[normalize-space()='To Give']//following-sibling::p")
    text_salesAmount_xpath = (By.XPATH, "//h2[contains(., 'Sales')]//following-sibling::p")
    text_purchaseAmount_xpath = (By.XPATH, "//h2[contains(., 'Purchase')]//following-sibling::p")
    text_expenseAmount_xpath = (By.XPATH, "//h2[contains(., 'Expense')]//following-sibling::p")
    text_netProfit_xpath = (By.XPATH, "//td[normalize-space()='Net Profit']//following-sibling::td")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
    
    def _extract_cleaned_amount(self, locator) -> str:
        amount_with_currency_and_comma =  conftest.getTextFromTextField(self.driver, locator)
        return amount_with_currency_and_comma.strip("Rs. ").replace(",", "")

    def get_to_receive_amount_from_dashboard(self) -> str:
        self.navigate_to_dashboard()
        return self._extract_cleaned_amount(self.text_toReceiveAmount_xpath)
    
    def get_to_give_amount_from_dashboard(self) -> str:
        self.navigate_to_dashboard()
        return self._extract_cleaned_amount(self.text_toGiveAmount_xpath)

    def get_sales_amount_from_dashboard(self) -> str:
        self.navigate_to_dashboard()
        return self._extract_cleaned_amount(self.text_salesAmount_xpath)

    def get_purchase_amount_from_dashboard(self) -> str:
        self.navigate_to_dashboard()
        return self._extract_cleaned_amount(self.text_purchaseAmount_xpath)

    def get_expense_amount_from_dashboard(self) -> str:
        self.navigate_to_dashboard()
        return self._extract_cleaned_amount(self.text_expenseAmount_xpath)

    def get_net_profit_from_profit_loss_report(self) -> str:
        self.navigate_to_profit_loss_report()
        return self._extract_cleaned_amount(self.text_netProfit_xpath)

