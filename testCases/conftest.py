import os
import shutil
import time
import logging
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from pageObjects.LoginPage import LoginPage
# from utilities.URLs import URLs
from utilities.customLogger import setup_logging
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from openpyxl import load_workbook

setup_logging()
@pytest.fixture()
def setup():
    global driver
    clean_allure_results()
    clear_log_file()
    browser = ReadConfig.getBrowser()

    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("safari"):
        driver = webdriver.Safari()
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

def headless_chrome():
    print()

def sendKeys(driver, locator, value, by=By.XPATH):
    try:
        logging.info(f"Sending keys by {by} with locator '{locator}'")
        waitForElement(driver, locator, by=by, timeout=10)
        driver.find_element(by, locator).send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        driver.find_element(by, locator).send_keys(value)
    except Exception as e:
        logging.error(f"An error occured in sendKeys when finding '{value}' with {by}: {locator}, {e}")

    
def findElement(driver, locator, by=By.XPATH, timeout=10):
    try:
        logging.info(f"Locating element by {by} with locator '{locator}'")
        waitForElement(driver, locator, by=by, timeout=10)
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))
    except TimeoutException:
        logging.error(f"Element with locator '{locator}' not found within {timeout} seconds")
        raise
    except NoSuchElementException:
        logging.error(f"Element with locator '{locator}' does not exist on the page")
        raise

def clickElement(driver, locator, by=By.XPATH):
    try:
        logging.info(f"Clicking an element by {by} with locator '{locator}'")
        waitForElement(driver, locator, by=by, timeout=10)
        driver.find_element(by, locator).click()
    except Exception as e:
        logging.error(f"An error occured in clickElement with {by}: {locator}, {e}")
        exit(1)

def clearInputField(driver, locator, by=By.XPATH):
    try:
        waitForElement(driver, locator, by=by, timeout=10)
        driver.find_element(by, locator).send_keys(Keys.CONTROL + "a" + Keys.DELETE)
    except Exception as e:
        logging.error(f"An error occured in clearInputField with {by}: {locator}, {e}")
        exit(1)

def getTextFromTextField(driver, locator, by=By.XPATH):
    try:
        waitForElement(driver, locator, by=by, timeout=10)
        return driver.find_element(by, locator).text
    except Exception as e:
        logging.error(f"An error occured in getTextFromTextField with {by}: {locator}, {e}")
        exit(1)

def clean_allure_results():
    results_dir = "AllureReport"
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    os.makedirs(results_dir)

def clear_log_file():
    with open('Configurations//Logs//revamp_karobar.log', 'w') as log_file:
        log_file.write('')

def waitForElement(driver, locator, by=By.XPATH, condition="visible", timeout=10):
    wait = WebDriverWait(driver, timeout)
    try:
        if condition == "clickable":
            return wait.until(EC.element_to_be_clickable((by, locator)))
        elif condition == "visible":
            return wait.until(EC.visibility_of_element_located((by, locator)))
        elif condition == "present":
            return wait.until(EC.presence_of_element_located((by, locator)))
        else:
            raise ValueError(
                f"Invalid condition '{condition}'. Use 'clickable', 'visible', or 'present'."
            )
    except Exception as e:
        print(f"Error while waiting for element: {e}")
        raise

def isElementPresent(driver: webdriver, locator, by=By.XPATH): 
    pass
        
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
    clickElement(driver, locator="//div[@role='dialog']//label[normalize-space()='As of Date']/following-sibling::button")

    # Locator of current month and year
    current_monthAndYear_element = "//div[@class='text-14 text-default font-medium']"
    
    # Locator of arrow button to change the month
    previuosMonth_xpath = "//button[@class='group rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft disabled:cursor-not-allowed bg-transparent hover:bg-surface active:bg-surface-hover font-medium text-16 absolute left-1 text-icon-active rounded-3 flex items-center justify-center h-9 w-9 p-0']"
    nextMonth_xpath = "//button[@class='group rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft disabled:cursor-not-allowed bg-transparent hover:bg-surface active:bg-surface-hover font-medium text-16 absolute right-1 text-icon-active rounded-3 flex items-center justify-center h-9 w-9 p-0']"
    while True:
        # Element to get the text of the current month and year
        monthAndYear = str(findElement(driver, current_monthAndYear_element, By.XPATH).text)
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