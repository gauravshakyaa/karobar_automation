import logging
import time
from selenium.webdriver.common.by import By
from utils import excel_utils
from utils.readProperties import ReadConfig
from testCases import conftest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class PaymentInOut:
    # Payment in/out page locators
    button_addPaymentInOut_xpath = (By.XPATH, "//button[normalize-space()='Add Payment In']")

    # Add payment in/out dialog locators
    inputField_receiptNumber_xpath = (By.XPATH,"//div[@role='dialog']//label[.='Receipt Number']//parent::div//following-sibling::div//input")
    datefield_date_xpath = (By.XPATH, "//div[@role='dialog']//label[normalize-space()='Date']")
    searchInputField_selectParty_name = (By.NAME, "party")
    inputField_totalAmount_name = (By.NAME, "totalAmount")
    dropdown_selectPaymentMode_xpath = (By.XPATH, "//div[@role='dialog']//select[@aria-hidden='true']")
    button_save_xpath = (By.XPATH, "//div[@role='dialog']//button[normalize-space()='Save Payment In']")
    button_saveAddNew_xpath = (By.XPATH, "//div[@role='dialog']//button[normalize-space()='Save & New']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = ReadConfig.getURL()

    def navigate_to_payment_in_out_page(self, transaction_type):
        if transaction_type == "in" or transaction_type == "payment in":
            if "payment-in" not in self.driver.current_url:
                self.driver.get(self.base_url + "/payment-in")
            else:
                logging.info("Already on Payment In page")
        elif transaction_type == "out" or transaction_type == "payment out":
            if "payment-out" not in self.driver.current_url:
                self.driver.get(self.base_url + "/payment-out")
            else:
                logging.info("Already on Payment Out page")
        else:
            logging.error("Invalid transaction type. Please provide either 'in' or 'out' argument in a transaction_type parameter")

    def open_addPaymentInOut_dialog(self, transaction_type):
        conftest.waitForElement(self.driver, self.searchInputField_selectParty_name, condition="all")
        if conftest.isElementPresent(self.driver, self.searchInputField_selectParty_name, timeout=2) is False:
            actions = ActionChains(self.driver)
            if transaction_type == "in" or transaction_type == "payment in":
                actions.key_down(Keys.ALT).send_keys('i').key_up(Keys.ALT).perform()
            else:
                actions.key_down(Keys.ALT).send_keys('o').key_up(Keys.ALT).perform()
        else:
            logging.info("Already on payment in/out dialog")
    
    def set_invoice_no(self, invoice_no):
        if conftest.isElementPresent(self.driver, self.inputField_receiptNumber_xpath):
            conftest.sendKeys(self.driver, self.inputField_receiptNumber_xpath, invoice_no)
        else:
            logging.error("Receipt number field not found in payment in/out dialog")

    def set_party(self, party_name):
        try:
            party_list__scrollable_container = "//div[@role='listbox']"
            select_party_locator = (By.XPATH, f"//div[@role='listbox']//div[.='{party_name}']")
            if conftest.isElementPresent(self.driver, self.searchInputField_selectParty_name):
                conftest.sendKeys(self.driver, self.searchInputField_selectParty_name, party_name)
                if conftest.scroll_until_element_visible(self.driver, element_locator=select_party_locator, scrollable_element_locator=party_list__scrollable_container, scroll_by=100):
                    conftest.clickElement(self.driver, select_party_locator)
                else:
                    logging.error("Party not found in the list")
        except Exception:
            logging.error("Error while selecting party in payment in/out dialog")
    
    def set_total_amount(self, total_amount):
        try:
            conftest.sendKeys(self.driver, self.inputField_totalAmount_name, total_amount)
        except Exception:
            logging.error("Error while setting total amount in payment in/out dialog")

    def set_payment_mode(self, payment_mode):
        try:
            payment_mode_dropdown = Select(self.driver.find_element(*self.dropdown_selectPaymentMode_xpath))
            payment_mode_dropdown.select_by_visible_text(payment_mode)
        except Exception:
            logging.error("Error while selecting payment mode in payment in/out dialog")
            exit(1)

    def click_save_button(self):
        try:
            conftest.clickElement(self.driver, self.button_saveAddNew_xpath)
        except Exception:
            conftest.clickElement(self.driver, self.button_save_xpath)
    
    def add_payment_in_out(self, transaction_type, party_name, invoice_no, total_amount, payment_mode):
        try:
            self.open_addPaymentInOut_dialog(transaction_type=transaction_type)
            self.set_party(party_name=party_name)
            self.set_invoice_no(invoice_no=invoice_no)
            self.set_total_amount(total_amount=total_amount)
            self.set_payment_mode(payment_mode=payment_mode)
        except Exception:
            logging.error(f"Error while adding payment in/out, transaction type: {transaction_type}, party: {party_name}, invoice no: {invoice_no}")
    
    def add_bulk_payment_in_out(self, transaction_type):
        payments_mapping_data = excel_utils.KEY_MAPPINGS["payment_in_out_key_mapping"]
        if transaction_type == "in" or transaction_type == "payment in":
            mapped_data = excel_utils.map_excel_keys(payments_mapping_data, sheet_name="Payments In Data")
        elif transaction_type == "out" or transaction_type == "payment out":
            mapped_data = excel_utils.map_excel_keys(payments_mapping_data, sheet_name="Payments Out Data")
        else:
            logging.error("Invalid transaction type")
        for data in mapped_data:
            self.add_payment_in_out(transaction_type=transaction_type, party_name=data["party_name"], invoice_no=data["invoice_no"], total_amount=data["total_amount"], payment_mode=data["payment_mode"])
            self.click_save_button()
            # assert "recorded successfully" in conftest.get_snackbar_message(self.driver)