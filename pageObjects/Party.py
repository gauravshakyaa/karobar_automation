from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException
from testCases import conftest

class Party:
    inputField_partyName_name = "fullName"
    inputField_partyPhoneNumber_name = "phoneNumber"
    radioButton_customerPartyType_xpath = f"//div[@role='dialog']//button[normalize-space()='Customer']"
    radioButton_supplierPartyType_xpath = f"//div[@role='dialog']//button[normalize-space()='Supplier']"
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

    button_saveParty_xpath = "//div[@role='dialog']//span[normalize-space()='Save Party']"
    button_saveAndNewPartyw_xpath = "//div[@role='dialog']//span[normalize-space()='Save & New']"
    
    def __init__(self, driver):
        self.driver = driver
        
    def setPartyName(self, name):
        conftest.sendKeys(self, self.inputField_partyName_name, name, By.NAME)
    
    def setPartyPhoneNo(self, name):
        conftest.sendKeys(self, self.inputField_partyPhoneNumber_name, name, By.NAME)
    
    def setCustomerPartyType(self):
        conftest.click(self, self.radioButton_customerPartyType_xpath, By.XPATH)
    
    def setSupplierPartyType(self):
        conftest.click(self, self.radioButton_supplierPartyType_xpath, By.XPATH)
    
    def setOpeningBalance(self, balance, balanceType):
        conftest.sendKeys(self, self.inputField_openingBalance_name, balance, By.NAME)
        if balanceType.lower() == "To Receive":
            conftest.click(self, self.button_toReceiveBalanceStatus_xpath, By.XPATH)
        elif balanceType.lower() == "To Give":
            conftest.click(self, self.button_toGiveBalanceStatus_xpath, By.XPATH)
        
    def setDate(self, date):
        conftest.click(self, self.datePicker_date_xpath, By.XPATH)
        conftest.sendKeys(self, self.datePicker_date_xpath, date, By.XPATH)
    
    def setPartyAddress(self, address):
        if conftest.isElementPresent(self, self.inputField_partyAddress_name, By.NAME):
            conftest.sendKeys(self, self.inputField_partyAddress_name, address, By.NAME)
    
    def setPartyEmail(self, email):
        conftest.sendKeys(self, self.inputField_partyEmail_name, email, By.NAME)
    
    def setPartyPan(self, pan):
        conftest.sendKeys(self, self.inputField_partyPan_name, pan, By.NAME)
    
    def clickSaveButton(self):
        conftest.click(self, "//div[@role='dialog']//button[normalize-space()='Save']", By.XPATH)
    
    def clickCancelButton(self):
        conftest.click(self, "//div[@role='dialog']//button[normalize-space()='Cancel']", By.XPATH)