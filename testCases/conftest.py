import os
import shutil
import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

@pytest.fixture()
def nav_to_dashboard():
    login_page =  LoginPage(driver)
    login_page.setPhoneNumber(ReadConfig.getPhoneNumber())
    login_page.clickContinueButton()
    login_page.setOTP(ReadConfig.getOTP())
    time.sleep(2)
    if "choose-account" in driver.current_url:
        login_page.selectBusiness(business_name="123")
    else:
        pass

def headless_chrome():
    print()

def sendKeys(driver, locator, value, clear_field=True):
    try:
        logging.info(f"Sending keys by locator {locator}")
        waitForElement(driver, locator, timeout=10)
        if clear_field:
            driver.find_element(*locator).send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        driver.find_element(*locator).send_keys(value)
    except Exception as e:
        logging.error(f"An error occured in sendKeys when sending '{value}' in locator {locator}")

    
def clickElement(driver, locator, by=None, timeout=10):
    if by is None:
        try:
            logging.info(f"Clicking an element with locator '{locator}'")
            waitForElement(driver, locator, timeout=timeout)
            driver.find_element(*locator).click() 
        except Exception as e:
            logging.error(f"An error occured in clickElement with locator {locator}")
    else:
        try:
            logging.info(f"Clicking an element with locator '{locator}' by {by}")
            waitForElement(driver, locator, by=by, timeout=timeout)
            driver.find_element(by, locator).click() 
        except Exception as e:
            logging.error(f"An error occured in clickElement with locator {locator}")

def clearInputField(driver, locator):
    try:
        waitForElement(driver, locator, timeout=10)
        driver.find_element(*locator).send_keys(Keys.CONTROL + "a" + Keys.DELETE)
    except Exception as e:
        logging.error(f"An error occured in clearInputField with locator {locator}")

def getTextFromTextField(driver, locator):
    try:
        waitForElement(driver, locator, timeout=10)
        return driver.find_element(*locator).text
    except Exception as e:
        logging.error(f"An error occured in getTextFromTextField with locator {locator}")

def get_snackbar_message(driver):
    try:
        snackbar_locator = (By.XPATH, "//li[@role='status']//div//div")
        return getTextFromTextField(driver, snackbar_locator)
    except Exception as e:
        logging.error(f"An error occured in return_snackbar_message: {e}")

def waitForElement(driver, locator, condition="visible", timeout=1):
    wait = WebDriverWait(driver, timeout)
    try:
        if condition == "clickable":
            return wait.until(EC.element_to_be_clickable(locator))
        elif condition == "visible":
            return wait.until(EC.visibility_of_element_located(locator))
        elif condition == "present":
            return wait.until(EC.presence_of_element_located(locator))
        elif condition == "all":
            # Custom callable function for combining multiple conditions
            def combined_condition():
                return (
                    EC.presence_of_element_located(locator) and
                    EC.visibility_of_element_located(locator) and
                    EC.element_to_be_clickable(locator)
                )
            return wait.until(combined_condition)
        else:
            raise ValueError(
                f"Invalid condition '{condition}'. Use 'clickable', 'visible', 'present', or 'all'."
            )
    except Exception as e:
        print("Error while waiting for element")
        raise

def isElementPresent(driver, locator, timeout=2): 
    try:
        wait = WebDriverWait(driver, timeout=timeout)
        wait.until(EC.visibility_of_element_located(locator))
        return True
    except Exception:
        return False
        exit(1)

def isElementEmpty(driver, locator, timeout=2):
    wait = WebDriverWait(driver, timeout=timeout)
    wait.until(EC.visibility_of_element_located(locator))
    if driver.find_element(*locator).text == "":
        return True
    else:
        return False

def scroll_until_element_visible(driver, element_locator, dropdown_element):
    while True:
        try:
            element = driver.find_element(*element_locator)
            if element.is_displayed():
                logging.info("Element is visible!")
                return True
        except Exception:
            pass  
        scrollable_element = driver.find_element(By.XPATH, dropdown_element)

        previous_scroll_height = driver.execute_script("return arguments[0].scrollTop;", scrollable_element)
        logging.info(f"Previous scroll height: {previous_scroll_height}")
        driver.execute_script("arguments[0].scrollTop += 180;", scrollable_element)
        
        new_scroll_height = driver.execute_script("return arguments[0].scrollTop;", scrollable_element)
        logging.info(f"New scroll height: {new_scroll_height}")
        if new_scroll_height == previous_scroll_height:
            logging.info("Reached the bottom of the page.")
            break
    return None  

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

def read_excel_file(file_path, sheet_name):
    pass