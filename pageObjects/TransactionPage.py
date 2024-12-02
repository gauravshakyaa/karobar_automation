from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException
from testCases import conftest

class CreateTransactionPage: # This includes Sales, Sales Return, Purchase, Purchase Return and Quotation
    searchField_selectParty_name = "party"
    inputField_invoice_xpath = "//input[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary w-full rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none text-16 h-11 px-3 py-2 bg-transparent']"
    datepicker_invoiceDate_xpath = "//button[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary w-full rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none px-3 py-2 bg-transparent relative pr-10 justify-between font-normal h-11 text-16']"
    # Item related locators
    itemTableColumn = 1  # by default, first column of the billing table will be assigned
    searchField_itemNAme_xpath = f"//tr[{itemTableColumn}]//input[@class='p-3 w-full h-full rounded-none outline-none bg-background hover:bg-secondary focus:ring-focus focus:ring-1 [&amp;::-webkit-outer-spin-button]:appearance-none [&amp;::-webkit-inner-spin-button]:appearance-none relative min-w-[25rem]']"
    inputField_quantity_xpath = f"//tbody/tr[{itemTableColumn}]/td[2]/div/input"
    inputField_rate_xpath = f"//tbody/tr[{itemTableColumn}]/td[3]/input"
    inputField_discountPercent_xpath = f"//tbody/tr[{itemTableColumn}]/td[4]/div/div[1]//input"
    inputField_discountAmount_xpath = f"//tbody/tr[{itemTableColumn}]/td[4]/div/div[2]//input"
    inputField_billingAmount_xpath = f"//tbody/tr[{itemTableColumn}]/td[5]//input"
    button_deleteBillingItem_xpath = f"//tbody/tr[{itemTableColumn}]/td[5]/span/button"
    # 'Add button' of Overall discount, TAX, Additional Charges, Round Off
    button_addDiscount_xpath = "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Add Discount']"
    button_addTAX_xpath = "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Add Tax']"
    button_addCharges_xpath = "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Add Charges']"
    button_addRoundOff_xpath = "//li[@class='flex flex-wrap gap-y-6 gap-x-8']//button[.='Round Off']"
    # Input field of discount, TAX Additional Charges and Round Off
    inputField_discountPercent_xpath = "//input[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none text-16 h-11 px-3 py-2 bg-background w-[100px] pr-7']"
    inputField_discountAmount_xpath = "//input[@class='flex items-center hover:border-hover hover:bg-secondary active:border-hover active:bg-secondary rounded-4 border border-border placeholder:text-default-tertiary text-default disabled:cursor-not-allowed disabled:bg-fill-primary-disabled disabled:placeholder:text-disabled disabled:text-disabled focus:outline-none focus:ring-2 focus:ring-focus focus:ring-offset-soft focus:ring-offset-2 [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none text-16 h-11 px-3 py-2 bg-background pl-10 w-[130px]"
    
    def __init__(self, driver):
        self.driver = driver