import logging
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
    
    button_addParty_xpath = "//button[normalize-space()='Add Party']"
    button_addNewFirstParty_xpath = "//button[normalize-space()='Add New Party']"

    def __init__(self, driver):
        self.driver = driver
        
    def setPartyName(self, name):
        conftest.sendKeys(self, self.inputField_partyName_name, name, By.NAME)
    
    def setPartyPhoneNo(self, name):
        conftest.sendKeys(self, self.inputField_partyPhoneNumber_name, name, By.NAME)
    
    def setCustomerPartyType(self):
        conftest.clickElement(self, self.radioButton_customerPartyType_xpath, By.XPATH)
    
    def setSupplierPartyType(self):
        conftest.clickElement(self, self.radioButton_supplierPartyType_xpath, By.XPATH)
    
    def setOpeningBalance(self, balance, balanceType):
        conftest.sendKeys(self, self.inputField_openingBalance_name, balance, By.NAME)
        if balanceType.lower() == "To Receive":
            conftest.clickElement(self, self.button_toReceiveBalanceStatus_xpath, By.XPATH)
        elif balanceType.lower() == "To Give":
            conftest.clickElement(self, self.button_toGiveBalanceStatus_xpath, By.XPATH)
        else:
            raise Exception("Invalid balance type")

    def setDate(self, day, month, year):
        month_mapping = {
            1: "Baisakh",
            2: "Jestha",
            3: "Asar",
            4: "Shrawan",
            5: "Bhadra",
            6: "Aswin",
            7: "Kartik",
            8: "Mangsir",
            9: "Poush",
            10: "Magh",
            11: "Falgun",
            12: "Chaitra",
        }
        # Clicks date picker to open date picker dialog
        conftest.clickElement(self.driver, self.datePicker_date_xpath)

        # Locator of current month and year
        current_monthAndYear_element = "//div[@class='text-14 text-default font-medium']"
       
        # Locator of arrow button to change the month
        previuosMonth_xpath = "//button[@class='group rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft disabled:cursor-not-allowed bg-transparent hover:bg-surface active:bg-surface-hover font-medium text-16 absolute left-1 text-icon-active rounded-3 flex items-center justify-center h-9 w-9 p-0']"
        nextMonth_xpath = "//button[@class='group rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft disabled:cursor-not-allowed bg-transparent hover:bg-surface active:bg-surface-hover font-medium text-16 absolute right-1 text-icon-active rounded-3 flex items-center justify-center h-9 w-9 p-0']"
        while True:
            # Element to get the text of the current month and year
            monthAndYear = str(conftest.findElement(self.driver, current_monthAndYear_element, By.XPATH).text)
            # Assigns current month and year to variables
            # Store month and year in string format
            current_month, current_year = monthAndYear.split()
            # If the current month and year match the desired month and year, exit the loop
            if str(current_month) == str(month_mapping[int(month)]) and int(current_year) == int(year):
                break
            # Navigate to the correct year and month
            if int(current_year) > int(year) or (int(current_year) == int(year) and month_mapping[int(month)] != current_month):
                # Move to the previous month
                conftest.clickElement(self.driver, previuosMonth_xpath)
            elif int(current_year) < int(year) or (int(current_year) == int(year) and month_mapping[int(month)] != current_month):
                # Move to the next month
                conftest.clickElement(self.driver, nextMonth_xpath)
        
        # Element to select the day as passed in the argument
        day_element = f"//span[@class='cursor-pointer rounded-3 flex items-center justify-center w-full aspect-square relative overflow-hidden p-0 font-normal text-center text-14'][normalize-space()='{day}']"
        conftest.clickElement(self.driver, day_element)

    def setPartyAddress(self, address):
        if conftest.isElementPresent(self, self.inputField_partyAddress_name, By.NAME):
            conftest.sendKeys(self, self.inputField_partyAddress_name, address, By.NAME)
    
    def setPartyEmail(self, email):
        conftest.sendKeys(self, self.inputField_partyEmail_name, email, By.NAME)
    
    def setPartyPan(self, pan):
        conftest.sendKeys(self, self.inputField_partyPan_name, pan, By.NAME)
    
    def clickSaveButton(self):
        conftest.clickElement(self.driver, "//div[@role='dialog']//button[normalize-space()='Save']", By.XPATH)
    
    def clickCancelButton(self):
        conftest.clickElement(self.driver, "//div[@role='dialog']//button[normalize-space()='Cancel']", By.XPATH)
    
    def openAddPartyDialog(self):
        pass
    
    def clickAddNewPartyButton(self):
        try:
            conftest.clickElement(self.driver, self.button_addParty_xpath)
        except Exception:
            conftest.clickElement(self.driver, self.button_addNewFirstParty_xpath)