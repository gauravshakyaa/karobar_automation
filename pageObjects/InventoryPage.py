import logging
import time
from selenium.webdriver.common.by import By
from utils import excel_utils
from utils.readProperties import ReadConfig
from testCases import conftest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class InventoryPage:
    ######### ADD/EDIT ITEM Page ##########
    inputField_itemName_name = (By.NAME, "name")
    searchField_itemCategory_css = (By.CSS_SELECTOR, "input[placeholder='Category']")
    radioButton_productItemType_css = (By.CSS_SELECTOR, "button[value='product']")
    radioButton_serviceItemType_css = (By.CSS_SELECTOR, "button[value='service']")
    inputField_openingStock_css = (By.CSS_SELECTOR, "input[name='openingStock']")
    # Unit related locator
    button_selectUnit_xpath = (By.XPATH, "//button[normalize-space()='Select Units']")
    dropdown_primaryUnit_xpath = (By.XPATH, "//div[@role='dialog']//label[text()='Primary Unit']")
    search_unit_xpath = (By.XPATH, "//input[@placeholder='Search Units']")
    dropdown_secondaryUnit_xpath = (By.XPATH, "//div[@role='dialog']//label[text()='Secondary Unit']")
    inputField_conversionRate_name = (By.NAME, "conversionRate")
    button_saveUnitDialog_xpath = (By.XPATH, "//div[@role='dialog']//button[.='Save']")
    button_cancelUnitDialog_xpath = (By.XPATH, "//div[@role='dialog']//button[.='Cancel']")
    
    inputField_salesPrice_xpath = (By.XPATH, "//input[@name='salesPrice']")
    inputField_purchasePrice_xpath = (By.XPATH, "//input[@name='purchasePrice']")

    switchButton_lowStockAlert_xpath = (By.XPATH, "//button[@role='switch'][@type='button']")
    inputField_lowStockQty_name = (By.NAME, "lowStockQuantity")

    # Locators for others tab
    tabList_stockDetailsTab_xpath = (By.XPATH, "//span[normalize-space()='Stock Details']")
    tabList_othersTab_xpath = (By.XPATH, "//span[normalize-space()='Others']")
    inputField_itemCode_name = (By.NAME, "code")
    inputField_description_name = (By.NAME, "description")
    inputField_location_name = (By.NAME, "itemLocation")
    image_itemImage_xpath = (By.XPATH, "//div[@aria-label='Upload Images']")

    button_save_css = (By.CSS_SELECTOR, "button[class*='inline-flex group relative rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft items-center justify-center disabled:cursor-not-allowed bg-fill-primary hover:bg-fill-primary-hover active:bg-fill-primary-active text-primary-on-bg-fill text-14 h-9 font-medium px-3 py-2 order-last']")
    button_saveAddNew_css = (By.CSS_SELECTOR, "button[class='inline-flex group relative rounded-4 outline-none gap-x-2 focus:ring-2 focus:ring-offset-2 focus:ring-focus focus:ring-offset-soft items-center justify-center disabled:cursor-not-allowed text-default border border-border text-14 h-9 font-medium px-3 py-2'] span")

    # Locators for item detail page
    searchField_searchItem_css = (By.CSS_SELECTOR, ".relative.flex-grow.flex.items-stretch input")
    list_itemDetail_xpath = "//div[@class='absolute top-0 left-0 w-full']//h3"
    button_adjustStock_xpath = (By.XPATH, "//div//button[.='Adjust Stock']")
    button_saveAddStock_xpath = (By.XPATH, "//div[contains(text(),'Add Stock')]")
    button_saveReduceStock_xpath = (By.XPATH, "//div[contains(text(),'Reduce Stock')]")

    # Locators for item adjustment dialog
    inputField_adjustmentQuantity_xpath = (By.XPATH, "//div[@role='dialog']//input[@name='quantity']")
    select_adjustmentItemUnit_xpath = (By.XPATH, "//div[@role='dialog']//select")
    inputField_adjustmentRate_xpath = (By.XPATH, "//div[@role='dialog']//input[@name='rate']")
    inputField_adjustmentNote_xpath = (By.XPATH, "//div[@role='dialog']//input[@name='note']")
    button_addReduceStock_xpath = (By.XPATH, "//div[@role='dialog']//button[@type='submit']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def setItemName(self, itemName):
        if conftest.isElementPresent(self.driver, self.inputField_itemName_name, timeout=1):
            conftest.sendKeys(self.driver, self.inputField_itemName_name, itemName)
        else:
            conftest.clickElement(self.driver, self.tabList_stockDetailsTab_xpath)
            conftest.sendKeys(self.driver, self.inputField_itemName_name, itemName)
    
    def setItemCategory(self, itemCategory):
        dropdown_itemCategory_xpath = (By.XPATH, f"//div[@role='listbox']//div[@role='option'][.='{itemCategory}']")
        dropdown_addNewItemCategory_xpath = (By.XPATH, "//div[@role='listbox']//div[@role='option']//span")
        if conftest.isElementPresent(self.driver, self.searchField_itemCategory_css, timeout=1):
            conftest.sendKeys(self.driver, self.searchField_itemCategory_css, itemCategory)
            if conftest.isElementPresent(self.driver, dropdown_itemCategory_xpath, timeout=1):
                conftest.clickElement(self.driver, dropdown_itemCategory_xpath)
            else:
                conftest.clickElement(self.driver, dropdown_addNewItemCategory_xpath)
        else:
            conftest.clickElement(self.driver, self.tabList_stockDetailsTab_xpath)
            conftest.sendKeys(self.driver, self.searchField_itemCategory_css, itemCategory)
            conftest.sendKeys(self.driver, self.searchField_itemCategory_css, itemCategory)
            if conftest.isElementPresent(self.driver, dropdown_itemCategory_xpath, timeout=1):
                conftest.clickElement(self.driver, dropdown_itemCategory_xpath)
            else:
                conftest.clickElement(self.driver, dropdown_addNewItemCategory_xpath)
    
    def setItemType(self, itemType):
        if itemType == "product" or itemType == "Product":
            pass
        else:
            if conftest.isElementPresent(self.driver, self.radioButton_serviceItemType_css, timeout=1):
                conftest.clickElement(self.driver, self.radioButton_serviceItemType_css)
            else:
                conftest.clickElement(self.driver, self.tabList_stockDetailsTab_xpath)
                conftest.clickElement(self.driver, self.radioButton_serviceItemType_css)

    def setOpeningStock(self, opening_qty):
        if conftest.isElementPresent(self.driver, self.inputField_openingStock_css, timeout=1):
            conftest.sendKeys(self.driver, self.inputField_openingStock_css, opening_qty)
        else:
            conftest.clickElement(self.driver, self.tabList_stockDetailsTab_xpath)
            conftest.sendKeys(self.driver, self.inputField_openingStock_css, opening_qty)

    def setSalesPrice(self, sales_price):
        if conftest.isElementPresent(self.driver, self.inputField_salesPrice_xpath, timeout=1):
            conftest.sendKeys(self.driver, self.inputField_salesPrice_xpath, sales_price)
        else:
            conftest.clickElement(self.driver, self.tabList_stockDetailsTab_xpath)
            conftest.sendKeys(self.driver, self.inputField_salesPrice_xpath, sales_price)

    def setPurchasePrice(self, purchase_price):
        if conftest.isElementPresent(self.driver, self.inputField_purchasePrice_xpath, timeout=1):
            conftest.sendKeys(self.driver, self.inputField_purchasePrice_xpath, purchase_price)
        else:
            conftest.clickElement(self.driver, self.tabList_stockDetailsTab_xpath)
            conftest.sendKeys(self.driver, self.inputField_purchasePrice_xpath, purchase_price)

    def setUnit(self, primary_unit=None, secondary_unit=None, conversionRate=None):
        def addUnit():
            if primary_unit:
                conftest.clickElement(self.driver, self.button_selectUnit_xpath)
                conftest.clickElement(self.driver, self.dropdown_primaryUnit_xpath)
                conftest.sendKeys(self.driver, self.search_unit_xpath, primary_unit)
                conftest.sendKeys(self.driver, self.search_unit_xpath, value=Keys.ENTER, clear_field=False)
                if secondary_unit:
                    conftest.clickElement(self.driver, self.dropdown_secondaryUnit_xpath)
                    conftest.sendKeys(self.driver, self.search_unit_xpath, secondary_unit)
                    conftest.sendKeys(self.driver, self.search_unit_xpath, value=Keys.ENTER, clear_field=False)
                    conftest.sendKeys(self.driver, self.inputField_conversionRate_name, conversionRate)
                else:
                    pass
                conftest.clickElement(self.driver, self.button_saveUnitDialog_xpath)

        if conftest.isElementPresent(self.driver, self.button_selectUnit_xpath, timeout=1):
            addUnit()
        else:
            conftest.clickElement(self.driver, self.tabList_stockDetailsTab_xpath)
            addUnit()


    def mrpPrice(self, mrp_price):
        pass

    def setSecondaryUnitPrice(self, secondary_unit_price):
        pass

    def setWholeSalePrice(self, whole_sale_price):
        pass

    def setMinWholesaleQty(self, min_wholesale_qty):
        pass

    def setLowStockAlert(self, low_stock_alert):
        if low_stock_alert:
            conftest.clickElement(self.driver, self.switchButton_lowStockAlert_xpath)
            conftest.sendKeys(self.driver, self.inputField_lowStockQty_name, low_stock_alert)

    def setItemCode(self, item_code):
        if conftest.isElementPresent(self.driver, self.inputField_itemCode_name, timeout=1):
            conftest.sendKeys(self.driver, self.inputField_itemCode_name, item_code)
        else:
            conftest.clickElement(self.driver, self.tabList_othersTab_xpath)
            conftest.sendKeys(self.driver, self.inputField_itemCode_name, item_code)
    
    def setLocation(self, location):
        if conftest.isElementPresent(self.driver, self.inputField_location_name, timeout=1):
            conftest.sendKeys(self.driver, self.inputField_location_name, location)
        else:
            conftest.clickElement(self.driver, self.tabList_othersTab_xpath)
            conftest.sendKeys(self.driver, self.inputField_location_name, location)

    def setDescription(self, description):
        if conftest.isElementPresent(self.driver, self.inputField_description_name, timeout=1):
            conftest.sendKeys(self.driver, self.inputField_description_name, description)
        else:
            conftest.clickElement(self.driver, self.tabList_othersTab_xpath)
            conftest.sendKeys(self.driver, self.inputField_description_name, description)

    def clickSaveButton(self):
        conftest.clickElement(self.driver, self.button_save_css)
    
    def clickSaveAddNewButton(self):
        conftest.clickElement(self.driver, self.button_saveAddNew_css)

    def navigateToAddEditItemPage(self):
        if "/inventory/add" in self.driver.current_url:
            pass
        else:
            self.driver.get(ReadConfig.getURL() + "/inventory/add")
    
    def addItem(self, itemName=None, itemCategory=None, itemType=None, openingStock=None, primary_unit=None, secondary_unit=None, conversionRate=None, salesPrice=None, purchasePrice=None, lowStockAlert=None, lowStockQty=None, itemCode=None, description=None, location=None):
        try:
            self.navigateToAddEditItemPage()
            if itemName:
                self.setItemName(itemName)
                if itemCategory:
                    self.setItemCategory(itemCategory)
                if itemType:
                    self.setItemType(itemType)
                if openingStock:
                    self.setOpeningStock(openingStock)
                if primary_unit:
                    self.setUnit(primary_unit, secondary_unit, conversionRate)
                if salesPrice:
                    self.setSalesPrice(salesPrice)
                if purchasePrice:
                    self.setPurchasePrice(purchasePrice)
                if itemCode:
                    self.setItemCode(itemCode)
                if description:
                    self.setDescription(description)
                if location:
                    self.setLocation(location)
        except Exception as e:
            logging.error(f"Error while adding item: {e}")
            exit(1)

    def navigateToItemDetailPage(self, item_name):
        def clickItem(item_name):
            scrollable_element_locator = "//div[@class='min-h-0 overflow-y-auto scrollbar-thin flex-grow']"
            list_items_locator = (By.XPATH, f"{self.list_itemDetail_xpath}[.='{item_name}']")
            conftest.sendKeys(self.driver, locator=self.searchField_searchItem_css, value=item_name, condition="all")
            conftest.waitForElement(self.driver, locator=list_items_locator, condition="visible")
            if conftest.scroll_until_element_visible(self.driver, element_locator=list_items_locator, scrollable_element_locator=scrollable_element_locator) is True:
                conftest.clickElement(self.driver, list_items_locator)
            else:
                logging.error(f"{item_name} not found in the list")
        if "/inventory/item-detail" in self.driver.current_url:
            clickItem(item_name)
        else:
            self.driver.get(ReadConfig.getURL() + "/inventory/item-detail/")
            clickItem(item_name)
    
    def addItemAdjustment(self, item_name, adjustment_type, adjustment_qty, rate = None, secondary_unit=None):
        self.navigateToItemDetailPage(item_name=item_name)
        time.sleep(0.2)
        conftest.clickElement(self.driver, self.button_adjustStock_xpath)
        if adjustment_type.lower() == "add":
            conftest.clickElement(self.driver, self.button_saveAddStock_xpath)
        elif adjustment_type.lower() == "reduce":
            conftest.clickElement(self.driver, self.button_saveReduceStock_xpath)
        else:
            logging.error("Invalid adjustment type")
            exit(1)
        conftest.sendKeys(self.driver, self.inputField_adjustmentQuantity_xpath, adjustment_qty)
        if secondary_unit == "SU":
            select_unit_locator = Select(self.driver.find_element(*self.select_adjustmentItemUnit_xpath))
            select_unit_locator.select_by_value("secondary")
        conftest.sendKeys(self.driver, self.inputField_adjustmentRate_xpath, rate)
        conftest.clickElement(self.driver, self.button_addReduceStock_xpath)
        conftest.waitForElement(self.driver, locator=self.inputField_adjustmentQuantity_xpath, condition="not_visible")
     
    def addBulkItems(self):
        item_mapping_data = excel_utils.KEY_MAPPINGS["item_key_mapping"]
        mapped_item_data = excel_utils.map_excel_keys(key_mapping=item_mapping_data, sheet_name="Item Data")
        for i, item_data in enumerate(mapped_item_data):
            self.addItem(**item_data)
            if i < len(mapped_item_data) - 1:
                self.clickSaveAddNewButton()
                time.sleep(0.2)
            else:
                self.clickSaveButton()

    def addBulkItemAdjustments(self):
        adjustment_mapping_data = excel_utils.KEY_MAPPINGS["item_adjustment_key_mapping"]
        mapped_adjustment_data = excel_utils.map_excel_keys(key_mapping=adjustment_mapping_data, sheet_name="Item Adjustment Data")
        for adjustment_data in mapped_adjustment_data:
            self.addItemAdjustment(item_name=adjustment_data["item_name"], adjustment_type=adjustment_data["adjustment_type"], adjustment_qty=adjustment_data["adjustment_qty"], rate=adjustment_data["rate"], secondary_unit=adjustment_data["secondary_unit"])
            
