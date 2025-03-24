import logging
import time
from selenium.webdriver.common.by import By
from utils import excel_utils
from utils.readProperties import ReadConfig
from testCases import conftest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from pageObjects.PaymentInOutPage import PaymentInOut
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class IncomeExpense(PaymentInOut):
    inputField_receiptNumber_xpath = (By.XPATH,"//div[@role='dialog']//label[.='Expense No.']//parent::div//following-sibling::div//input")
    searchInputField_category_name = (By.NAME, "category")
    button_addIncomeExpense_xpath = (By.XPATH, "//button[@class='inline-flex group relative rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft items-center justify-center disabled:cursor-not-allowed bg-fill-primary hover:bg-fill-primary-hover active:bg-fill-primary-active text-primary-on-bg-fill text-14 h-9 font-medium px-3 py-2']")
    dialog_expense_xpath = (By.XPATH, "//div[@role='dialog']//div//h2[.='Add Expense']")
    dialog_income_xpath = (By.XPATH, "//div[@role='dialog']//div//h2[.='Add Income']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def set_category(self, category):
        try:
            scrollable_container = "//div[@role='listbox']"
            category_element_locator = (By.XPATH, f"//div[@role='listbox']//div[.='{category}']")
            conftest.sendKeys(self.driver, self.searchInputField_category_name, category)
            if conftest.scroll_until_element_visible(self.driver, element_locator=category_element_locator, scrollable_element_locator=scrollable_container):
                conftest.clickElement(self.driver, category_element_locator)
            else:
                logging.error(f"Unable to find category '{category}' in dropdown")
        except Exception:
            logging.error("Error while setting category")
    
    def navigate_to_income_expense_page(self, transaction_type):
        if transaction_type == "expense":
            if "expense" not in self.driver.current_url:
                self.driver.get(self.base_url + "/expense")
            else:
                logging.info("Already on Expense page. Continuing...")
        elif transaction_type == "income":
            if "income" not in self.driver.current_url:
                self.driver.get(self.base_url + "/income")
                logging.info("Already on Income page. Continuing...")
        else:
            logging.error("Invalid transaction type. Please provide either 'expense' or 'income' argument in a transaction_type parameter")

    def click_add_income_expense_button(self, transaction_type):
        if conftest.isElementPresent(self.driver, self.dialog_expense_xpath, timeout=2) or conftest.isElementPresent(self.driver, self.dialog_income_xpath, timeout=2):
            pass
        else:
            self.navigate_to_income_expense_page(transaction_type)
            time.sleep(2)
            assert transaction_type in self.driver.current_url
            try:
                conftest.clickElement(self.driver, self.button_addIncomeExpense_xpath)
            except Exception:
                logging.error("Unable to click Add New Expense button")
    
    def add_income_expense(self, transaction_type, category, number, total_amount, payment_mode):
        self.click_add_income_expense_button(transaction_type)
        self.set_category(category)
        self.set_invoice_no(number)
        self.set_total_amount(total_amount)
        self.set_payment_mode(payment_mode)

    def add_bulk_income_expense(self, transaction_type):
        income_expense_mapping_data = excel_utils.KEY_MAPPINGS["income_expense_key_mapping"]
        if transaction_type == "expense":
            mapped_data = excel_utils.map_excel_keys(income_expense_mapping_data, sheet_name="Expenses Data")
        elif transaction_type == "income":
            mapped_data = excel_utils.map_excel_keys(income_expense_mapping_data, sheet_name="Other Income Data")
        else:
            logging.error("Invalid transaction type")
        for data in mapped_data:
            self.add_income_expense(transaction_type, category=data["category"], number=data["number"], total_amount=data["total_amount"], payment_mode=data["payment_mode"])
            self.click_save_button()