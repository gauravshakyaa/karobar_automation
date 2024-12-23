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
        
    def setDate(self, day, month, year):
        month_mapping = {
        "baisakh": 1,
        "jestha": 2,
        "ashad": 3,
        "shrawan": 4,
        "bhadra": 5,
        "ashwin": 6,
        "kartik": 7,
        "mangsir": 8,
        "poush": 9,
        "magh": 10,
        "falgun": 11,
        "chaitra": 12,
}
        conftest.click(self, self.datePicker_date_xpath, By.XPATH)
        # Locator of current month and year
        current_monthAndYear_element = "//div[@class='text-14 text-default font-medium']"
        
        # Element to select the day as passed in the argument
        day_element = f"//span[@class='cursor-pointer rounded-3 flex items-center justify-center w-full aspect-square relative overflow-hidden p-0 font-normal text-center text-14'][normalize-space()='{day}']"
        
        # Element to get the text of the current month and year
        monthAndYear = conftest.findElement(self, current_monthAndYear_element, By.XPATH).text
        
        # Assigns current month and year to variables
        current_month, current_year = monthAndYear.split()
        
        # Locator of arrow button to change the month
        previuosMonth_xpath = "//button[@class='group rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft disabled:cursor-not-allowed bg-transparent hover:bg-surface active:bg-surface-hover font-medium text-16 absolute left-1 text-icon-active rounded-3 flex items-center justify-center h-9 w-9 p-0']"
        nextMonth_xpath = "//button[@class='group rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft disabled:cursor-not-allowed bg-transparent hover:bg-surface active:bg-surface-hover font-medium text-16 absolute right-1 text-icon-active rounded-3 flex items-center justify-center h-9 w-9 p-0']"
        while True:
            if year == current_year:
                break
            elif year < current_year:
                conftest.clickElement(self, previuosMonth_xpath)
            else:
                conftest.clickElement(self, nextMonth_xpath)

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
    
