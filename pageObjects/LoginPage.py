from selenium.webdriver.common.by import By
from testCases import conftest

class LoginPage:
    # Locators for Login Page
    textfield_phoneNumber_name = "phoneNumber"
    button_continue_xpath = "//button[@type='submit']"
    button_continueWithGoogle_xpath = "//button[contains(@class,'inline-flex group relative rounded-4 outline-none gap-x-2 focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-focus focus-visible:ring-offset-soft items-center justify-center disabled:cursor-not-allowed text-default bg-surface hover:bg-surface-hover active:bg-surface-active font-medium text-16 px-5 py-2.5')]"

    textfieldValidation_phoneNumber_xpath = "//span[@class='text-error']"

    # Locators for OPT verification page
    textfield_opt_id = "otp-verification"
    button_verifyOTP_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setPhoneNumber(self, number):
        conftest.sendKeys(driver=self.driver, locator=self.textfield_phoneNumber_name, value=number, by=By.NAME)
    
    def clickContinueButton(self):
        conftest.clickElement(self.driver, self.button_continue_xpath)
        
    def returnPhoneTextFieldErrorMessage(self):
        return conftest.getTextFromTextField(self.driver, self.textfieldValidation_phoneNumber_xpath)

    def setOTP(self, otp):
        conftest.sendKeys(driver=self.driver, locator=self.textfield_opt_id, value=otp, by=By.ID)
        # No need to click Verify OTP button because it automatically submits the button

    