import logging
import time
from selenium.webdriver.common.by import By
from utils import excel_utils
from utils.readProperties import ReadConfig
from testCases import conftest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

class ManageAccount:
    # Manage Account page locators
    button_addAccount_xpath = (By.XPATH, "//button[normalize-space()='Add Account']")
    cardView_cashAccount_xpath = (By.XPATH, "//a[contains(.,'Cash')]")

    # Add Account dialog locators
    dropdown_selectAccountType_xpath = (By.XPATH, "//div[@role='dialog']//select[@aria-hidden='true']")
    inputField_accountName_name = (By.NAME, "accountName")
    inputField_accountNumber_name = (By.NAME, "accountId") 
    inputField_accountHolderName_name = (By.NAME, "accountHolder")
    inputField_openingBalance_name = (By.NAME, "balance")
    button_saveAccount_css = (By.CSS_SELECTOR, "button[type='submit']")

    # Adjust Balance button locators
    button_adjustBalance_xpath = (By.XPATH, "//button[contains(normalize-space(),'Adjust Balance')]")
    button_addMoney_xpath = (By.XPATH, "//div[@role='menu']//div[.='Add Money']")
    button_reduceMoney_xpath = (By.XPATH, "//div[@role='menu']//div[.='Reduce Money']")
    button_transferMoney_xpath = (By.XPATH, "//div[@role='menu']//div[.='Transfer Money']")

    # Adjust Balance (Add/Reduce) dialog locators
    radiobutton_typeAddMoney_xpath = (By.XPATH, "//div[@role='dialog']//div[@role='radiogroup']//button[@value='add-money']")
    radiobutton_typeReduceMoney_xpath = (By.XPATH, "//div[@role='dialog']//div[@role='radiogroup']//button[@value='reduce-money']")
    dropdown_selectAddReduceAccount_xpath = (By.XPATH, "//div[@role='dialog']//label[normalize-space()='Account']//following::select[@aria-hidden='true']")
    inputField_totalAmount_name = (By.NAME, "totalAmount")
    button_saveAdjustBalance_xpath = (By.XPATH, "//div[@role='dialog']//button[@type='submit']")

    # Adjust Balance (Transfer) dialog locators
    dropdown_selectFromAccount_xpath = (By.XPATH, "//label[normalize-space()='Transfer From']//following-sibling::select")
    dropdown_selectToAccount_xpath = (By.XPATH, "//label[normalize-space()='Transfer To']//following-sibling::select")

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def navigate_to_manage_account(self):
        if 'manage-account' not in self.driver.current_url:
            self.driver.get(ReadConfig.getURL() + "/manage-account")
            conftest.clickElement(self.driver, self.cardView_cashAccount_xpath)
        else:
            logging.info("Already on manage account page")

    def add_account(self, account_type, account_name, account_number=123, account_holder_name="Guided Tester", opening_balance=None):
        def add_new_account():
            if account_type.lower() != "cash":
                conftest.clickElement(self.driver, self.button_addAccount_xpath)
                select = Select(self.driver.find_element(*self.dropdown_selectAccountType_xpath))
                select.select_by_value(account_type.lower())
                conftest.sendKeys(self.driver, self.inputField_accountName_name, account_name)
                conftest.sendKeys(self.driver, self.inputField_accountNumber_name, account_number)
                if account_type.lower() == "bank":
                    if account_holder_name:
                        conftest.sendKeys(self.driver, self.inputField_accountHolderName_name, account_holder_name)
                if opening_balance:
                    conftest.sendKeys(self.driver, self.inputField_openingBalance_name, opening_balance)
                conftest.clickElement(self.driver, self.button_saveAccount_css)
            else:
                logging.warning("Cash account already exists. Skipping adding a new account.")
        # Starts here
        logging.info("Adding a new account")
        self.navigate_to_manage_account()
        add_new_account()
    
    def add_bulk_accounts(self):
        account_mapping_data = excel_utils.KEY_MAPPINGS["accounts_key_mapping"]
        mapped_account_data = excel_utils.map_excel_keys(account_mapping_data, sheet_name="Bank Accounts Data")
        for account_data in mapped_account_data:
            self.add_account(account_data["account_type"], account_data["account_name"])

    def add_reduce_money(self, adjustment_type, from_account_name, amount, to_account_name=None):
        try:
            def add_reduce_money():
                conftest.waitForElement(self.driver, self.radiobutton_typeAddMoney_xpath)
                select = Select(self.driver.find_element(*self.dropdown_selectAddReduceAccount_xpath))
                select.select_by_visible_text(from_account_name)
                conftest.sendKeys(self.driver, self.inputField_totalAmount_name, amount)
                conftest.clickElement(self.driver, self.button_saveAdjustBalance_xpath)
            self.navigate_to_manage_account()
            conftest.clickElement(self.driver, self.cardView_cashAccount_xpath)
            conftest.clickElement(self.driver, self.button_adjustBalance_xpath, condition="clickable")
            if conftest.isElementPresent(self.driver, self.button_addMoney_xpath):
                if adjustment_type.lower() == "add":  
                    conftest.clickElement(self.driver, self.button_addMoney_xpath)
                    logging.info(f"Adding amount {amount} to {from_account_name}")
                    add_reduce_money()
                elif adjustment_type.lower() == "reduce":
                    conftest.clickElement(self.driver, self.button_reduceMoney_xpath)
                    logging.info(f"Reducing amount {amount} from {from_account_name}")
                    add_reduce_money()
                elif adjustment_type.lower() == "transfer":
                    conftest.clickElement(self.driver, self.button_transferMoney_xpath)
                    logging.info(f"Transferring amount {amount} from {from_account_name} to {to_account_name}")
                    select_from_account = Select(self.driver.find_element(*self.dropdown_selectFromAccount_xpath))
                    select_from_account.select_by_visible_text(from_account_name)
                    select_to_account = Select(self.driver.find_element(*self.dropdown_selectToAccount_xpath))
                    select_to_account.select_by_visible_text(to_account_name)
                    conftest.sendKeys(self.driver, self.inputField_totalAmount_name, amount)
                    conftest.clickElement(self.driver, self.button_saveAdjustBalance_xpath)
                else:
                    logging.error("Invalid account type provided. Please provide a valid account type.")
                    return
            else:
                logging.error("Add/Reduce/Transfer button not found. Please check if the element is loaded properly.")
        except Exception as e:
            logging.error(f"Error occurred while adding/reducing/transferring money: {e}")

    def add_bulk_account_adjustments(self):
        account_adjustment_mapping_data = excel_utils.KEY_MAPPINGS["accounts_adjustment_key_mapping"]
        mapped_account_adjustment_data = excel_utils.map_excel_keys(key_mapping=account_adjustment_mapping_data, sheet_name="Transaction Adjustment Data")
        for account_adjustment_data in mapped_account_adjustment_data:
            self.add_reduce_money(adjustment_type=account_adjustment_data["adjustment_type"], from_account_name=account_adjustment_data["from_account_name"], 
                                  amount=account_adjustment_data["amount"], 
                                  to_account_name=account_adjustment_data["to_account_name"]) 
