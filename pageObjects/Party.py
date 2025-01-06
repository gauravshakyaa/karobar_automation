import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException
from testCases import conftest
from selenium.webdriver.chrome.webdriver import WebDriver

class Party:
    ######### ADD PARTY DIALOG ##########
    inputField_partyName_name = "fullName"
    inputField_partyPhoneNumber_name = "phoneNumber"
    radioButton_customerPartyType_xpath = "//div[@role='dialog']//button[normalize-space()='Customer']"
    radioButton_supplierPartyType_xpath = "//div[@role='dialog']//button[normalize-space()='Supplier']"
    # 'Credit Info' locators
    tabList_creditInfo_xpath = "//div[@role='dialog']//div[@role='tablist']//button[1]"
    tabList_additionalInfo_xpath = "//div[@role='dialog']//div[@role='tablist']//button[2]"
    inputField_openingBalance_name = "openingBalance"
    datePicker_date_xpath = "//div[@role='dialog']//label[normalize-space()='As of Date']/following-sibling::button"
    button_toReceiveBalanceStatus_xpath = "//div[@role='dialog']//button[@value='To Receive']"
    button_toGiveBalanceStatus_xpath = "//div[@role='dialog']//button[@value='To Give']"
    # 'Additional Info' locators
    button_additionalInfo_xpath = "//span[normalize-space()='Additional Info']"
    inputField_partyAddress_name = "partyAddress"
    inputField_partyEmail_name = "partyEmail"
    inputField_partyPan_name = "panNo"

    button_saveParty_xpath = "//div[@role='dialog']//button[normalize-space()='Save Party']"
    button_saveAndNewParty_xpath = "//div[@role='dialog']//span[normalize-space()='Save & New']"
    
    button_addParty_xpath = "//button[normalize-space()='Add Party']"
    button_addNewFirstParty_xpath = "//button[normalize-space()='Add New Party']"

    ######### PARTY LIST/DETAIL PAGE ##########
    listView_partiesList_xpath = "//div[@class='min-h-0 overflow-y-auto scrollbar-thin flex-grow']"

    def __init__(self, driver):
        self.driver : WebDriver = driver
        
    def setPartyName(self, name):
        conftest.sendKeys(self.driver, self.inputField_partyName_name, value=name, by=By.NAME)
    
    def setPartyPhoneNo(self, name):
        conftest.sendKeys(self.driver, self.inputField_partyPhoneNumber_name, value=name, by=By.NAME)
    
    def setCustomerPartyType(self):
        conftest.clickElement(self.driver, self.radioButton_customerPartyType_xpath)
    
    def setSupplierPartyType(self):
        conftest.clickElement(self.driver, self.radioButton_supplierPartyType_xpath)
    
    def setOpeningBalance(self, balance, balanceType  : str):
        conftest.sendKeys(self.driver, self.inputField_openingBalance_name, balance, By.NAME)
        if balanceType.lower() == "to receive":
            conftest.clickElement(self.driver, self.button_toReceiveBalanceStatus_xpath)
        elif balanceType.lower() == "to give":
            conftest.clickElement(self.driver, self.button_toGiveBalanceStatus_xpath)
        else:
            logging.error("Invalid balance type")
            raise Exception("Invalid balance type")

    def setPartyAddress(self, address):
        if conftest.isElementPresent(self.driver, self.inputField_partyAddress_name, by=By.NAME, timeout=5):
            conftest.sendKeys(self.driver, self.inputField_partyAddress_name, address, By.NAME)
        else:
            conftest.clickElement(self.driver, self.button_additionalInfo_xpath, By.XPATH)
            conftest.sendKeys(self.driver, self.inputField_partyAddress_name, address, By.NAME)

    def setPartyEmail(self, email):
        if conftest.isElementPresent(self.driver, self.inputField_partyEmail_name, By.NAME, timeout=5):
            conftest.sendKeys(self.driver, self.inputField_partyEmail_name, email, By.NAME)
        else:
            conftest.clickElement(self.driver, self.button_additionalInfo_xpath, By.XPATH)
            conftest.sendKeys(self.driver, self.inputField_partyEmail_name, email, By.NAME)
    
    def setPartyPan(self, pan):
        if conftest.isElementPresent(self.driver, self.inputField_partyPan_name, By.NAME, timeout=5):
            conftest.sendKeys(self.driver, self.inputField_partyPan_name, pan, By.NAME)
        else:
            conftest.clickElement(self.driver, self.button_additionalInfo_xpath, By.XPATH)
            conftest.sendKeys(self.driver, self.inputField_partyPan_name, pan, By.NAME)
        
    
    def clickSaveButton(self):
        conftest.clickElement(self.driver, self.button_saveParty_xpath, By.XPATH)
    
    def clickSaveAddNewButton(self):
        conftest.clickElement(self.driver, self.button_saveAndNewParty_xpath, By.XPATH)
    
    def clickAddNewPartyButton(self):
        try:
            time.sleep(1)
            conftest.clickElement(self.driver, self.button_addParty_xpath)
        except Exception:
            time.sleep(1)
            conftest.clickElement(self.driver, self.button_addNewFirstParty_xpath)
    
    def openAddPartyDialog(self):
        if self.driver.current_url ==  f"{ReadConfig.getURL()}/parties":
            time.sleep(1)
            self.clickAddNewPartyButton()
        else:
            time.sleep(1)
            self.driver.get(ReadConfig.getURL() + "/parties")
            self.clickAddNewPartyButton()
    
    def addParty(self, name=None, phone=None, partyType=None, balance=None, balanceType=None, address=None, email=None, pan=None):
        self.openAddPartyDialog()
        if name:
            self.setPartyName(name)
        if phone:
            self.setPartyPhoneNo(phone)
        if partyType:
            if partyType.lower() == "customer":
                self.setCustomerPartyType()
            elif partyType.lower() == "supplier":
                self.setSupplierPartyType()
            else:
                raise Exception("Invalid party type while adding party")
                exit(1)
        if balance:
            self.setOpeningBalance(balance, balanceType)
        if address:
            self.setPartyAddress(address)
        if email:
            self.setPartyEmail(email)
        if pan:
            self.setPartyPan(pan)
        