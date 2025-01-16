from selenium.webdriver.common.by import By
from utils.readProperties import ReadConfig
from testCases import conftest
import logging
from selenium.webdriver.chrome.webdriver import WebDriver

class CreateTransactionPage: # This includes Sales, Sales Return, Purchase, Purchase Return and Quotation
    # Party-related locators
    searchField_selectParty_name = (By.NAME, "party")
    inputField_invoice_xpath = (By.XPATH, "//input[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary w-full rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none text-16 h-11 px-3 py-2 bg-transparent']")
    datepicker_invoiceDate_xpath = (By.XPATH, "//button[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary w-full rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none px-3 py-2 bg-transparent relative pr-10 justify-between font-normal h-11 text-16']")

    # Item-related locators
    itemTableColumnIndex = 1  # By default, first column of the billing table will be assigned
    searchField_itemName_xpath = (By.XPATH, f"//tr[{itemTableColumnIndex}]//input[@class='p-3 w-full h-full rounded-none outline-none bg-background hover:bg-secondary focus:ring-focus focus:ring-1 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none relative min-w-[25rem]']")
    inputField_quantity_xpath = (By.XPATH, f"//tbody/tr[{itemTableColumnIndex}]/td[2]/div/input")
    inputField_rate_xpath = (By.XPATH, f"//tbody/tr[{itemTableColumnIndex}]/td[3]/input")
    inputField_discountPercent_xpath = (By.XPATH, f"//tbody/tr[{itemTableColumnIndex}]/td[4]/div/div[1]//input")
    inputField_discountAmount_xpath = (By.XPATH, f"//tbody/tr[{itemTableColumnIndex}]/td[4]/div/div[2]//input")
    inputField_billingAmount_xpath = (By.XPATH, f"//tbody/tr[{itemTableColumnIndex}]/td[5]//input")
    button_deleteBillingItem_xpath = (By.XPATH, f"//tbody/tr[{itemTableColumnIndex}]/td[5]/span/button")

    # Buttons for overall discount, tax, additional charges, and round-off
    button_addDiscount_xpath = (By.XPATH, "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Add Discount']")
    button_addTAX_xpath = (By.XPATH, "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Add Tax']")
    button_addCharges_xpath = (By.XPATH, "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Add Charges']")
    button_addRoundOff_xpath = (By.XPATH, "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Round Off']")

    # Input fields for discount, tax, additional charges, and round-off
    inputField_discountPercent_xpath = (By.XPATH, "//input[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none text-16 h-11 px-3 py-2 bg-background w-[100px] pr-7']")
    inputField_discountAmount_xpath = (By.XPATH, "//input[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none text-16 h-11 px-3 py-2 bg-background pl-10 w-[130px]']")
    
    def __init__(self, driver):
        self.driver : WebDriver = driver

    def setParty(self, name):
        try:
            logging.info(f"Selecting party: {name}")
            conftest.sendKeys(self.driver, self.searchField_selectParty_name, name)
        except Exception as e:
            logging.error(f"Error while selecting party: {e}")
            raise
    
    def setInvoiceNumber(self, invoice_number):
        try:
            logging.info(f"Setting invoice number: {invoice_number}")
            conftest.sendKeys(self.driver, self.inputField_invoice_xpath, value = invoice_number)
        except Exception as e:
            logging.error(f"Error while setting invoice number: {e}")
            raise
    
    def navigateToCreateTransactionPage(self):
        try:
            if self.driver.current_url == ReadConfig.getURL() + "/sales-invoices/create":
                pass
            else:
                pass
        except Exception as e:
            logging.error(f"Error while navigating to create transaction page: {e}")
            raise