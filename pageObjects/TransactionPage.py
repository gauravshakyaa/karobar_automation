import json
from selenium.webdriver.common.by import By
from utils import excel_utils
from utils.readProperties import ReadConfig
from testCases import conftest
import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

class TransactionPage: # This includes Sales, Sales Return, Purchase, Purchase Return and Quotation
    # Party-related locators
    searchField_selectParty_name = (By.NAME, "party")
    inputField_invoice_xpath = (By.XPATH, "//input[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary w-full rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none text-16 h-11 px-3 py-2 bg-transparent']")
    datepicker_invoiceDate_xpath = (By.XPATH, "//button[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary w-full rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none px-3 py-2 bg-transparent relative pr-10 justify-between font-normal h-11 text-16']")

    # Buttons for overall discount, tax, additional charges, and round-off
    button_addOverallDiscount_xpath = (By.XPATH, "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Add Discount']")
    button_addTAX_xpath = (By.XPATH, "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Add Tax']")
    button_addCharges_xpath = (By.XPATH, "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[contains(.,'Charges')]")
    button_addRoundOff_xpath = (By.XPATH, "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Round Off']")

    # Input fields for overall discount, tax, additional charges, and round-off
    inputField_overallDiscountPercent_xpath = (By.XPATH, "//input[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none text-16 h-11 px-3 py-2 bg-background w-[100px] pr-7']")
    inputField_overallDiscountAmount_xpath = (By.XPATH, "//input[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none text-16 h-11 px-3 py-2 bg-background pl-10 w-[130px]']")

    inputField_total_name = (By.NAME, "totalAmount")
    inputField_usedAmount_xpath = (By.NAME, "receivedAmount")

    button_paymentMode_xpath = (By.XPATH, "//label[normalize-space()='Payment Mode']//following-sibling::div//select")
    
    button_saveAddNew_css = (By.CSS_SELECTOR, "button[class='inline-flex group relative rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft items-center justify-center disabled:cursor-not-allowed text-default border border-border font-medium text-16 px-5 py-2.5 -order-1']")
    button_save_css = (By.CSS_SELECTOR, "button[class='inline-flex group relative rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft items-center justify-center disabled:cursor-not-allowed bg-fill-primary hover:bg-fill-primary-hover active:bg-fill-primary-active text-primary-on-bg-fill font-medium text-16 px-5 py-2.5 rounded-tr-none rounded-br-none']")
    
    
    def __init__(self, driver):
        self.driver : WebDriver = driver

    def setParty(self, name):
        try:
            party_dropdown_listbox = "//div[@role='listbox']"
            party_dropdown_list = (By.XPATH, f"//div[@role='listbox']//div//div[text()='{name}']")
            if "Cash" in name:
                party_dropdown_list = (By.XPATH, "//div[@role='listbox']//div[1]//div[1]")
                logging.info("Selecting Cash as party")
                conftest.clickElement(self.driver, party_dropdown_list)
            else:
                logging.info(f"Selecting party: {name}")
                conftest.sendKeys(self.driver, self.searchField_selectParty_name, name)
                self.driver.implicitly_wait(1)
                if conftest.scroll_until_element_visible(self.driver, element_locator=party_dropdown_list, dropdown_element=party_dropdown_listbox):
                    conftest.clickElement(self.driver, party_dropdown_list)
        except Exception as e:
            logging.error(f"Error while selecting party: {e}")
    
    def setInvoiceNumber(self, invoice_number):
        try:
            logging.info(f"Setting invoice number: {invoice_number}")
            conftest.sendKeys(self.driver, self.inputField_invoice_xpath, value = invoice_number)
        except Exception as e:
            logging.error(f"Error while setting invoice number: {e}")

    def set_billing_item(self, items):
        try:
            def set_single_item_details(index, item_name, quantity=None, secondary_unit=None, rate=None, discount_percent=None, discount_amount=None):
                billing_item_dropdown_list = (By.XPATH, f"//div[@role='option']//div[@class='flex gap-3 items-center col-span-2']//p[contains(text(), '{item_name}')]")
                searchField_itemName_xpath = (By.CSS_SELECTOR, f"tr input[name='invoiceItems.{int(index)-1}.name']")
                inputField_quantity_xpath = (By.XPATH, f"//tbody/tr[{index}]/td[3]/div/input")
                # button_unit_xpath = (By.XPATH, f"//tbody/tr[{index}]/td[2]/div//button")
                select_unit_xpath = (By.XPATH, f"//tbody/tr[{index}]/td[3]/div//select")
                inputField_rate_xpath = (By.XPATH, f"//tbody/tr[{index}]/td[4]/input")
                inputField_itemDiscountPercent_xpath = (By.XPATH, f"//tbody/tr[{index}]/td[5]/div/div[1]//input")
                inputField_itemDiscountAmount_xpath = (By.XPATH, f"//tbody/tr[{index}]/td[5]/div/div[2]//input")
                # inputField_billingAmount_xpath = (By.XPATH, f"//tbody/tr[{index}]/td[5]//input") # Total amount field not in use right now
                # button_deleteBillingItem_xpath = (By.XPATH, f"//tbody/tr[{index}]/td[5]/span/button") # Delete button not in use right now
                if item_name:
                    logging.info(f"Adding billing item: {item_name}")
                    conftest.sendKeys(self.driver, searchField_itemName_xpath, value = item_name)
                    conftest.clickElement(self.driver, billing_item_dropdown_list)
                    if quantity:
                        conftest.sendKeys(self.driver, inputField_quantity_xpath, value = quantity)
                    if secondary_unit:
                        try:
                            select_unit = Select(self.driver.find_element(*select_unit_xpath))
                            select_unit.select_by_visible_text(secondary_unit)
                        except Exception as e:
                            logging.warning(f"Failed to select unit '{secondary_unit}' for item '{item_name}': {e}")
                    if rate:
                        conftest.sendKeys(self.driver, inputField_rate_xpath, value = rate)
                    if discount_percent:
                        conftest.sendKeys(self.driver, inputField_itemDiscountPercent_xpath, value = discount_percent)
                    if discount_amount:
                        conftest.sendKeys(self.driver, inputField_itemDiscountAmount_xpath, value = discount_amount)
                else:
                    logging.error("Please provide item name to add billing item")
            for index, item in enumerate(items, start=1):
                set_single_item_details(
                    index=index,
                    item_name=item.get("item_name"),
                    quantity=item.get("quantity"),
                    secondary_unit=item.get("secondary_unit"), 
                    rate=item.get("rate"),
                    discount_percent=item.get("item_discount_percent"),
                    discount_amount=item.get("item_discount_amount") 
                )
        except Exception as e:
            logging.error(f"Error while adding billing item: {e}")
        
    def setOverallDiscount(self, discount_percent=None, discount_amount=None):
        try:
            if discount_percent:
                if conftest.isElementPresent(self.driver, self.inputField_overallDiscountPercent_xpath):
                    conftest.sendKeys(self.driver, self.inputField_overallDiscountPercent_xpath, value = discount_percent)
                else:
                    conftest.clickElement(self.driver, self.button_addOverallDiscount_xpath)
                    conftest.sendKeys(self.driver, self.inputField_overallDiscountPercent_xpath, value = discount_percent)
            if discount_amount:
                if conftest.isElementPresent(self.driver, self.inputField_overallDiscountAmount_xpath):
                    conftest.sendKeys(self.driver, self.inputField_overallDiscountAmount_xpath, value = discount_amount)
                else:
                    conftest.clickElement(self.driver, self.button_addOverallDiscount_xpath)
                    conftest.sendKeys(self.driver, self.inputField_overallDiscountAmount_xpath, value = discount_amount)
        except Exception as e:
            logging.error(f"Error while setting overall discount: {e}")

    def setTax(self):
        try:
            conftest.clickElement(self.driver, self.button_addTAX_xpath)
        except Exception as e:
            logging.error(f"Error while setting tax: {e}")

    def setCharges(self, charge_name="Charge", charge_amount=None):
        try:
            for i, charge in enumerate(charge_amount):
                inputField_chargeName_xpath = (By.XPATH, f"//ul//li[{i+1}]//input[@placeholder='Enter charge name']")
                inputField_chargeAmount_xpath = (By.XPATH, f"//ul//li[{i+1}]//input[@placeholder='Enter charge name']//following-sibling::div//input")
                charge_name_value = f"{charge_name} {i+1}"
                conftest.clickElement(self.driver, self.button_addCharges_xpath)
                conftest.sendKeys(self.driver, inputField_chargeName_xpath, value = charge_name_value)
                conftest.sendKeys(self.driver, inputField_chargeAmount_xpath, value = charge)

        except Exception as e:
            logging.error(f"Error while setting charges: {e}")

    def setTotalAmount(self, total_amount):
        try:
            conftest.sendKeys(self.driver, self.inputField_total_name, value = total_amount)
        except Exception as e:
            logging.error(f"Error while setting total amount: {e}")
    
    def setUsedAmount(self, used_amount):
        try:
            conftest.sendKeys(self.driver, self.inputField_usedAmount_xpath, value = used_amount)
        except Exception as e:
            logging.error(f"Error while setting used amount: {e}")

    def setPaymentMode(self, payment_mode):
        try:
            selectpayment_mode = Select(self.driver.find_element(*self.button_paymentMode_xpath))
            selectpayment_mode.select_by_visible_text(payment_mode)
        except Exception as e:
            logging.error(f"Error while setting payment mode: {e}")

    def clickSaveButton(self):
        try:
            conftest.clickElement(self.driver, self.button_save_css)
        except Exception as e:
            logging.error(f"Error while clicking save button: {e}")
    
    def clickSaveAndNewButton(self):
        try:
            conftest.clickElement(self.driver, self.button_saveAddNew_css)
        except Exception as e:
            logging.error(f"Error while clicking save and new button: {e}")

    def navigateToCreateTransactionPage(self, transaction_type):
        try:
            base_url = ReadConfig.getURL()
            transaction_url_map = {
                "s": "/sales-invoices/create",
                "p": "/purchase/create",
                "sr": "/sales-return/create",
                "pr": "/purchase-return/create",
                "q": "/quotations/create",
            }
            target_url = base_url + transaction_url_map[transaction_type]
            if self.driver.current_url == target_url + transaction_url_map[transaction_type]:
                pass
            else:
                self.driver.get(target_url)
        except Exception as e:
            logging.error(f"Error while navigating to create transaction page: {e}")

    def addTransaction(self, transaction_type, party_name = None, invoice_number = None, items=None, overall_discount_percent = None, overall_discount_amount = None, tax=None, charge_name=None, charge_amount = None, round_off_amount = None, total_amount=None, used_amount=None, payment_mode=None):
        self.navigateToCreateTransactionPage(transaction_type=transaction_type)
        if party_name:
            self.setParty(name=party_name)
        if invoice_number:
            self.setInvoiceNumber(invoice_number=invoice_number)
        if items:
            self.set_billing_item(items=items)
        if items:
            if overall_discount_percent:
                self.setOverallDiscount(discount_percent=overall_discount_percent)
            if overall_discount_amount:
                self.setOverallDiscount(discount_amount=overall_discount_amount)
        if items:
            if tax is True:
                self.setTax()
        if items:
            if charge_amount:
                self.setCharges(charge_amount=charge_amount)
        if not items:
            if total_amount:
                self.setTotalAmount(total_amount=total_amount)
        if "Cash" not in party_name:
            if used_amount:
                self.setUsedAmount(used_amount=used_amount)
        if payment_mode:
            self.setPaymentMode(payment_mode=payment_mode)
    
    def addBulkTransactions(self, transaction_type=None):
        transaction_json_data = json.loads(excel_utils.get_transaction_details_json(transaction_type=transaction_type))
        for transaction in transaction_json_data:
            invoice_number = transaction.get("invoice_number")
            party_name = transaction.get("party_name")
            billing_details = transaction.get("Billing Details", [])
            total_amount = transaction.get("total_amount")
            used_amount = transaction.get("used_amount")
            payment_mode = transaction.get("payment_mode")
            overall_discount_percent = transaction.get("overall_discount_percent")
            overall_discount_amount = transaction.get("overall_discount_amount")
            tax = bool(transaction.get("tax"))
            charge_amount = transaction.get("charge_amount") if transaction.get("charge_amount") else None
            self.addTransaction(
                transaction_type=transaction_type,
                party_name=party_name,
                invoice_number=invoice_number,
                items=billing_details,  # Pass full list
                overall_discount_percent=overall_discount_percent,
                overall_discount_amount=overall_discount_amount,
                tax=tax,
                charge_amount=charge_amount,
                total_amount=total_amount,
                used_amount=used_amount,
                payment_mode=payment_mode
            )
            self.clickSaveAndNewButton()
            snackbar_message = conftest.get_snackbar_message(self.driver)
            logging.info(f"Snackbar message: {snackbar_message}")
            self.driver.implicitly_wait(0.5)