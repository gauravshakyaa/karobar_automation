from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException
from testCases import conftest

class Party:
    inputField_partyName_name = "fullName"
    inputField_partyNumber_name = "phoneNumber"
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
    inputField_partyAddress_name = "partyAddress"
    inputField_partyEmail_name = "partyEmail"
    inputField_partyPan_name = "panNo"
    
    def __init__(self, driver):
        self.driver = driver
        
    def setPartyName(self, name):
        conftest.sendKeys(self, self.inputField_partyName_name, name, By.NAME)
    
    
