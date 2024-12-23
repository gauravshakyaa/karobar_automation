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

setup_logging()
@pytest.fixture()
def setup():
    global driver
    clean_allure_results()
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
    time.sleep(5)
    yield driver
    logging.info("All driver quited.")
    driver.quit()

@pytest.fixture()
def nav_to_dashboard(setup):
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
    with open(f"{os.getcwd}/revamp_karobar.log", "w"):
        pass 

def waitForElement(driver, locator, by=By.XPATH, condition="clickable", timeout=10):
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
