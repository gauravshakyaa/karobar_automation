from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException
from testCases import conftest

class PaymentInOut:
    inputField_receiptNumber_xpath = "//div[@role='dialog']//label[.='Receipt Number']/following-sibling::div"
    datefield_date_xpath = "//label[normalize-space()='Date']"
    searchInputField_selectParty_xpath = "//div[@role='dialog']//label[normalize-space()='Party Name']/parent::div/following-sibling::div//input"
    inputField_totalAmount_xpath = "//form[1]/div[1]/div[1]/div[4]/div[1]/div[1]//input"