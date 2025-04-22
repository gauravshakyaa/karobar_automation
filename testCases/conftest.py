import os
import shutil
import logging
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, WebDriverException
from utils.customLogger import setup_logging
from utils.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )

setup_logging()
@pytest.fixture()
def setup(request):
    global driver
    headless_mode = request.config.getoption("--headless")
    clean_allure_results()
    clear_log_file()
    browser = ReadConfig.getBrowser()
    options = webdriver.ChromeOptions()
    if headless_mode and options:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-blink-features=AutomationControlled")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome(options=options)
    elif browser.__eq__("edge"):
        driver = webdriver.Edge(options=options)
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox(options=options)
    elif browser.__eq__("safari"):
        driver = webdriver.Safari(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.get(f"{ReadConfig.getURL()}")
    driver.maximize_window()
    yield driver
    logging.info("All driver quited.")
    driver.quit()

@pytest.fixture
def nav_to_dashboard(setup):
    driver = setup
    login_page =  LoginPage(driver)
    login_page.setPhoneNumber(ReadConfig.getPhoneNumber())
    login_page.clickContinueButton()
    login_page.setOTP(ReadConfig.getOTP())
    waitForElement(driver, login_page.text_selectProfile_xpath, timeout=3)
    if "choose-account" in driver.current_url:
        logging.info("Select business page is displayed. Continuing...")
        login_page.selectBusiness(business_name="offline data test")
        logging.info("Business selected successfully.")
    elif "account-setup" in driver.current_url:
        logging.info("Setup account page is displayed. Continuing...")
        login_page.create_business(account_name="Automation", business_name="Automation")
        logging.info("Business created successfully.")

def headless_chrome():
    print()

def get_text_from_attribute(driver, locator, attribute, log_exception=True):
    try:
        waitForElement(driver, locator, timeout=3)
        return driver.find_element(*locator).get_attribute(attribute)
    except Exception as e:
        handle_exception(exception=e, locator=locator, extra_message="while getting text from attribute.", log_exception=log_exception)

def sendKeys(driver, locator, value, clear_field=True, condition="visible", timeout=3, log_exception=True):
    try: 
        logging.info(f"Sending keys by locator {locator}, value: {value}")
        waitForElement(driver, locator, timeout=timeout, condition=condition)
        if clear_field:
            driver.find_element(*locator).send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        driver.find_element(*locator).send_keys(value)
    except Exception as e:
        handle_exception(exception=e, locator=locator, value=value, extra_message="while sending keys.", log_exception=log_exception)

    
def clickElement(driver, locator, by=None, timeout=3, condition="visible", log_exception=True):
    try:
        if by is None:
            logging.info(f"Clicking an element with locator '{locator}'")
            waitForElement(driver, locator, timeout=timeout, condition=condition)
            driver.find_element(*locator).click()
        else:
            logging.info(f"Clicking an element with locator '{locator}' by {by}")
            waitForElement(driver, locator, by=by, timeout=timeout, condition=condition)
            driver.find_element(by, locator).click() 
    except Exception as e:
        handle_exception(exception=e, locator=locator, extra_message="while clicking an element.", log_exception=log_exception)
    
def clearInputField(driver, locator):
    try:
        waitForElement(driver, locator, timeout=3)
        driver.find_element(*locator).send_keys(Keys.CONTROL + "a" + Keys.DELETE)
    except Exception as e:
        handle_exception(exception=e, locator=locator, extra_message="while clearing input field.")

def send_keyboard_keys(driver, locator, keys):
    try:
        waitForElement(driver, locator, timeout=3)
        driver.find_element(*locator).send_keys(keys)
    except Exception as e:
        handle_exception(exception=e, locator=locator, extra_message="while sending enter key.")

def getTextFromTextField(driver, locator):
    try:
        waitForElement(driver, locator, timeout=3)
        return driver.find_element(*locator).text
    except Exception as e:
        handle_exception(exception=e, locator=locator, extra_message="while getting text for the element.")

def get_snackbar_message(driver):
    try:
        snackbar_locator = (By.XPATH, "//li[@role='status']//div//div[1]")
        return getTextFromTextField(driver, snackbar_locator)
    except Exception as e:
        logging.error(f"An error occured in return_snackbar_message: {e}")

def waitForElement(driver, locator, condition="visible", timeout=3, text=None):
    wait = WebDriverWait(driver, timeout)
    try:
        conditions = {
        "clickable": EC.element_to_be_clickable(locator),
        "visible": EC.visibility_of_element_located(locator),
        "present": EC.presence_of_element_located(locator),
        "not_visible": EC.invisibility_of_element_located(locator),
        "text": EC.text_to_be_present_in_element(locator, text),
        "all": lambda driver: (
                EC.presence_of_element_located(locator)(driver) and
                EC.visibility_of_element_located(locator)(driver) and
                EC.element_to_be_clickable(locator)(driver)
            )
        }
        if condition not in conditions:
            raise ValueError(f"Invalid condition: {condition}")
        return wait.until(conditions[condition])
    except Exception:
        return False

def isElementPresent(driver, locator, timeout=3, condition="visible"): 
    try:
        if waitForElement(driver, locator=locator, condition=condition, timeout=timeout):
            return True
        else:
            return False
    except Exception:
        return False

def isElementEmpty(driver, locator, timeout=2):
    wait = WebDriverWait(driver, timeout=timeout)
    wait.until(EC.visibility_of_element_located(locator))
    if driver.find_element(*locator).text == "":
        return True
    else:
        return False

def scroll_until_element_visible(driver, element_locator, scrollable_element_locator, scroll_by=500, timeout=3):
    scrollable_element = driver.find_element(By.XPATH, scrollable_element_locator)
    first_location = driver.execute_script("return arguments[0].scrollTop;", scrollable_element)
    logging.debug(f"First location: {first_location}")
    if first_location > 0:
        logging.debug("Scrolling to the top.")
        driver.execute_script("arguments[0].scrollTop = 0;", scrollable_element)
    while True:
        try:
            waitForElement(driver, locator=element_locator, timeout=timeout, condition="all")
            element = driver.find_element(*element_locator)
            if element.is_displayed():
                logging.info("Element is visible!")
                return True
        except Exception:
            pass  
        previous_scroll_height = driver.execute_script("return arguments[0].scrollTop;", scrollable_element)
        driver.execute_script(f"arguments[0].scrollTop += {scroll_by};", scrollable_element)
        waitForElement(driver, element_locator, timeout=2, condition="clickable")
        new_scroll_height = driver.execute_script("return arguments[0].scrollTop;", scrollable_element)
        if new_scroll_height == previous_scroll_height:
            logging.info("Reached the bottom of the page.")
            break
    return False

def handle_exception(exception, locator=None, value=None, extra_message=None, log_exception=True):
    if log_exception:
        error_message = ""
        if locator and value:
            error_message = f" Locator: {locator}, Value: {value}, {extra_message}"
        if isinstance(exception, NoSuchElementException):
            logging.error(f"Error: The specified element was not found on the page.{error_message}, locator: {locator}")
        elif isinstance(exception, TimeoutException):
            logging.error(f"Error: The operation timed out while waiting for the element.{error_message}, locator: {locator}")
        elif isinstance(exception, ElementNotInteractableException):
            logging.error(f"Error: The element is present but not interactable.{error_message}, locator: {locator}")
        elif isinstance(exception, StaleElementReferenceException):
            logging.error(f"Error: The element is no longer attached to the DOM.{error_message}, locator: {locator}")
        elif isinstance(exception, WebDriverException):
            logging.error(f"Error: A general WebDriver error occurred. Locator: {locator}, {error_message}")
        else:
            logging.error(f"Unexpected Error: {exception}{error_message}")

def clean_allure_results():
    results_dir = "AllureReport"
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    os.makedirs(results_dir)

def clear_log_file():
    with open('Configurations//Logs//revamp_karobar.log', 'w') as log_file:
        log_file.write('')

def setDate(day, month, year):
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
    clickElement(driver, locator = "//div[@role='dialog']//label[normalize-space()='As of Date']/following-sibling::button")

    # Locator of current month and year
    current_monthAndYear_element = "//div[@class='text-14 text-default font-medium']"
    
    # Locator of arrow button to change the month
    previuosMonth_xpath = "//button[@class='group rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft disabled:cursor-not-allowed bg-transparent hover:bg-surface active:bg-surface-hover font-medium text-16 absolute left-1 text-icon-active rounded-3 flex items-center justify-center h-9 w-9 p-0']"
    nextMonth_xpath = "//button[@class='group rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft disabled:cursor-not-allowed bg-transparent hover:bg-surface active:bg-surface-hover font-medium text-16 absolute right-1 text-icon-active rounded-3 flex items-center justify-center h-9 w-9 p-0']"
    while True:
        # Element to get the text of the current month and year
        monthAndYear = str(getTextFromTextField(driver, current_monthAndYear_element))
        # Assigns current month and year to variables
        # Store month and year in string format
        current_month, current_year = monthAndYear.split()
        # If the current month and year match the desired month and year, exit the loop
        if str(current_month) == str(month_mapping[int(month)]) and int(current_year) == int(year):
            break
        # Navigate to the correct year and month
        if int(current_year) > int(year) or (int(current_year) == int(year) and month_mapping[int(month)] != current_month):
            # Move to the previous month
            clickElement(driver, previuosMonth_xpath)
        elif int(current_year) < int(year) or (int(current_year) == int(year) and month_mapping[int(month)] != current_month):
            # Move to the next month
            clickElement(driver, nextMonth_xpath)
    
    # Element to select the day as passed in the argument
    day_element = f"//span[@class='cursor-pointer rounded-3 flex items-center justify-center w-full aspect-square relative overflow-hidden p-0 font-normal text-center text-14'][normalize-space()='{day}']"
    clickElement(driver, day_element)

