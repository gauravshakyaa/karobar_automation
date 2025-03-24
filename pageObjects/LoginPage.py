from selenium.webdriver.common.by import By
from testCases import conftest

class LoginPage:
    # Locators for Login Page
    textfield_phoneNumber_name = (By.NAME, 'phoneNumber')
    button_continue_xpath = (By.XPATH, "//button[@type='submit']")
    button_continueWithGoogle_xpath = (By.XPATH, "//button[contains(@class,'inline-flex group relative rounded-4 outline-none gap-x-2 focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-focus focus-visible:ring-offset-soft items-center justify-center disabled:cursor-not-allowed text-default bg-surface hover:bg-surface-hover active:bg-surface-active font-medium text-16 px-5 py-2.5')]")
    textfieldValidation_phoneNumber_xpath = (By.XPATH, "//span[@class='text-error']")

    # Locators for OPT verification page
    textfield_opt_id = (By.ID, "otp-verification")
    button_verifyOTP_xpath = (By.XPATH, "//button[@type='submit']")

    # Locators for choose business page
    text_selectProfile_xpath = (By.XPATH, "//h2[normalize-space()='Select Profile']")

    def __init__(self, driver):
        self.driver = driver

    def setPhoneNumber(self, number):
        conftest.sendKeys(self.driver, self.textfield_phoneNumber_name, value=number)
    
    def clickContinueButton(self):
        conftest.clickElement(self.driver, self.button_continue_xpath)
        
    def returnPhoneTextFieldErrorMessage(self):
        return conftest.getTextFromTextField(self.driver, self.textfieldValidation_phoneNumber_xpath)

    def setOTP(self, otp):
        conftest.sendKeys(self.driver, self.textfield_opt_id, value=otp)
        # No need to click Verify OTP button because it automatically submits the button

    def selectBusiness(self, business_name=None, index=None, business_role=None):
        locator = "//div[contains(@class,'md:pl-12 md:-ml-12 py-1.5 flex flex-col gap-y-4 mt-8 pr-1 max-h-[485px] overflow-y-auto scrollbar-thin ')]"
        if business_name:
            real_locator = (By.XPATH, f"{locator}//h2[contains(text(),'{business_name}')]")
            conftest.clickElement(self.driver, real_locator)
        elif index:
            locator += f"//button[{index}]"
            conftest.clickElement(self.driver, locator)