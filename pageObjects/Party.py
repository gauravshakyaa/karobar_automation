import datetime
import logging
import time
from selenium.webdriver.common.by import By
from utils import excel_utils
from utils.readProperties import ReadConfig
from testCases import conftest
from selenium.webdriver.remote.webdriver import WebDriver

class Party:
    # ADD PARTY DIALOG #
    inputField_partyName_name = (By.NAME, "fullName")
    inputField_partyPhoneNumber_name = (By.NAME, "phoneNumber")
    radioButton_customerPartyType_xpath = (By.XPATH, "//div[@role='dialog']//button[normalize-space()='Customer']")
    radioButton_supplierPartyType_xpath = (By.XPATH, "//div[@role='dialog']//button[normalize-space()='Supplier']")
    # 'Credit Info' locators
    tabList_creditInfo_xpath = (By.XPATH, "//div[@role='dialog']//div[@role='tablist']//button[1]")
    tabList_additionalInfo_xpath = (By.XPATH, "//div[@role='dialog']//div[@role='tablist']//button[2]")
    inputField_openingBalance_name = (By.NAME, "openingBalance")
    datePicker_date_xpath = (By.XPATH, "//div[@role='dialog']//label[normalize-space()='As of Date']/following-sibling::button")
    button_toReceiveBalanceStatus_xpath = (By.XPATH, "//div[@role='dialog']//button[@value='To Receive']")
    button_toGiveBalanceStatus_xpath = (By.XPATH, "//div[@role='dialog']//button[@value='To Give']")
    # 'Additional Info' locators
    button_additionalInfo_xpath = (By.XPATH, "//span[normalize-space()='Additional Info']")
    inputField_partyAddress_name = (By.NAME, "partyAddress")
    inputField_partyEmail_name = (By.NAME, "partyEmail")
    inputField_partyPan_name = (By.NAME, "panNo")

    button_saveParty_xpath = (By.XPATH, "//div[@role='dialog']//button[normalize-space()='Save Party']")
    button_saveAndNewParty_xpath = (By.XPATH, "//div[@role='dialog']//span[normalize-space()='Save & New']")

    button_addParty_xpath = (By.XPATH, "//button[normalize-space()='Add Party']")
    button_addNewFirstParty_xpath = (By.XPATH, "//button[normalize-space()='Add New Party']")

    wait_forPartyButton_xpath = "//button[contains(., 'Party')]"

    # PARTY LIST/DETAIL PAGE #
    listView_partiesList_xpath = (By.XPATH, "//div[@class='min-h-0 overflow-y-auto scrollbar-thin flex-grow']")

    def __init__(self, driver):
        self.driver : WebDriver = driver
        
    def setPartyName(self, name):
        conftest.sendKeys(self.driver, self.inputField_partyName_name, value=name)

    def setPartyPhoneNo(self, name):
        conftest.sendKeys(self.driver, self.inputField_partyPhoneNumber_name, value=name)
    
    def setCustomerPartyType(self):
        conftest.clickElement(self.driver, self.radioButton_customerPartyType_xpath)
    
    def setSupplierPartyType(self):
        conftest.clickElement(self.driver, self.radioButton_supplierPartyType_xpath)
    
    def setOpeningBalance(self, balance, balanceType  : str):
        conftest.sendKeys(self.driver, self.inputField_openingBalance_name, balance)
        if balanceType.lower() == "receivable":
            conftest.clickElement(self.driver, self.button_toReceiveBalanceStatus_xpath)
        elif balanceType.lower() == "payable":
            conftest.clickElement(self.driver, self.button_toGiveBalanceStatus_xpath)
        else:
            logging.error("Invalid balance type")
            raise Exception("Invalid balance type")

    def setPartyAddress(self, address):
        if conftest.isElementPresent(self.driver, self.inputField_partyAddress_name, timeout=0.5):
            conftest.sendKeys(self.driver, self.inputField_partyAddress_name, address)
        else:
            conftest.clickElement(self.driver, self.button_additionalInfo_xpath)
            conftest.sendKeys(self.driver, self.inputField_partyAddress_name, address)

    def setPartyEmail(self, email):
        if conftest.isElementPresent(self.driver, self.inputField_partyEmail_name, timeout=0.5):
            conftest.sendKeys(self.driver, self.inputField_partyEmail_name, email)
        else:
            conftest.clickElement(self.driver, self.button_additionalInfo_xpath)
            conftest.sendKeys(self.driver, self.inputField_partyEmail_name, email)
    
    def setPartyPan(self, pan):
        if conftest.isElementPresent(self.driver, self.inputField_partyPan_name, timeout=0.5):
            conftest.sendKeys(self.driver, self.inputField_partyPan_name, pan)
        else:
            conftest.clickElement(self.driver, self.button_additionalInfo_xpath)
            conftest.sendKeys(self.driver, self.inputField_partyPan_name, pan)
    
    def clickSaveButton(self):
        if conftest.isElementPresent(self.driver, self.button_saveParty_xpath, timeout=0.5):
            conftest.clickElement(self.driver, self.button_saveParty_xpath)
        else:
            conftest.clickElement(self.driver, self.button_saveAndNewParty_xpath)

    def clickSaveAddNewButton(self):
        if conftest.isElementPresent(self.driver, self.button_saveAndNewParty_xpath, timeout=0.5):
            conftest.clickElement(self.driver, self.button_saveAndNewParty_xpath, timeout=0.5)
        else:
            conftest.clickElement(self.driver, self.button_saveParty_xpath, timeout=0.5)

    def clickAddNewPartyButton(self):
        if not conftest.isElementPresent(self.driver, locator="//div[@role='dialog']//h2[contains(.,'Party')]", timeout=0): # If already on party dialog, skip the process
            try:
                if conftest.isElementPresent(self.driver, self.button_addParty_xpath, timeout=0.5):
                    conftest.clickElement(self.driver, self.button_addParty_xpath)
                else:
                    conftest.clickElement(self.driver, self.button_addNewFirstParty_xpath)
            except Exception:
                pass
        else:
            pass
    
    def openAddPartyDialog(self):
        if conftest.isElementPresent(self.driver, locator="//div[@role='dialog']//h2[contains(.,'Party')]", timeout=0) is False: # If not in party dialog, open add party dialog
            try:
                if "/parties" in self.driver.current_url:
                    time.sleep(1)
                    # conftest.waitForElement(self.driver, self.wait_forPartyButton_xpath, timeout=1)
                    self.clickAddNewPartyButton()
                else:
                    self.driver.get(ReadConfig.getURL() + "/parties")
                    time.sleep(1)
                    # conftest.waitForElement(self.driver, self.wait_forPartyButton_xpath, timeout=1)
                    self.clickAddNewPartyButton()
            except Exception:
                pass
        else:
            pass
        
    def addParty(self, name=None, phone=None, partyType=None, balance=None, balanceType=None, address=None, email=None, pan=None):
        self.openAddPartyDialog()
        if name:
            self.setPartyName(name)
        if phone:
            self.setPartyPhoneNo(phone)
        if partyType:
            if partyType.lower() == "customer":
                pass
            elif partyType.lower() == "supplier":
                self.setSupplierPartyType()
            else:
                raise Exception("Invalid party type while adding party")
        if balance:
            self.setOpeningBalance(balance, balanceType)
        if address:
            self.setPartyAddress(address)
        if email:
            self.setPartyEmail(email)
        if pan:
            self.setPartyPan(pan)
    
    def addBulkParty(self):
        party_map_data = excel_utils.KEY_MAPPINGS["party_key_mapping"]
        mapped_party_data = excel_utils.map_excel_keys(key_mapping=party_map_data, sheet_name="Party Data")
        total_time = 0
        for i, party_data in enumerate(mapped_party_data):
            self.addParty(**party_data)
            if i < len(mapped_party_data) - 1:
                self.clickSaveAddNewButton()
            else:
                self.clickSaveButton()