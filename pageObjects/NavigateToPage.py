import logging
from utils.readProperties import ReadConfig
from selenium.webdriver.remote.webdriver import WebDriver
from testCases import conftest
from selenium.webdriver.common.by import By

class NavigateToPage:
    def __init__(self, driver):
        self.driver : WebDriver = driver
        self.base_url = ReadConfig.getURL()
        self.parties_list = self.base_url + "/parties"

        self.item_list = self.base_url + "/inventory"
        self.item_detail = self.base_url + "/inventory/item-detail"
        self.add_item = self.base_url + "/inventory/add"

        self.sales_list = self.base_url + "/sales-invoices"
        self.add_sales = self.base_url + "/sales-invoices/create"
        self.payment_in_list = self.base_url + "/payment-in"
        self.quotation_list = self.base_url + "/quotations"
        self.add_quotation = self.base_url + "/quotations/create"
        self.sales_return_list = self.base_url + "/sales-return"
        self.add_sales_return = self.base_url + "/sales-return/create"

        self.purchase_list = self.base_url + "/purchase"
        self.add_purchase = self.base_url + "/purchase/create"
        self.payment_out_list = self.base_url + "/payment-out"
        self.purchase_return_list = self.base_url + "/purchase-return"
        self.add_purchase_return = self.base_url + "/purchase-return/create"

        self.expenses_list = self.base_url + "/expense"
        self.income_list = self.base_url + "/income"
        
        self.accounts_list = self.base_url + "/manage-account"

        self.reports_list = self.base_url + "/reports"
        self.sales_report = self.base_url + "/reports/sales"
        self.purchase_report = self.base_url + "/reports/purchase"
        self.sales_return_report = self.base_url + "/reports/sales-return"
        self.purchase_return_report = self.base_url + "/reports/purchase-return"
        self.data_book_report = self.base_url + "/reports/day-book"
        self.all_transactions_report = self.base_url + "/reports/all-transactions"
        self.profit_loss_report = self.base_url + "/reports/profit-and-loss"
        self.party_statement_report = self.base_url + "/reports/party-statement"
        self.all_parties_report = self.base_url + "/reports/all-party"
        self.item_details_report = self.base_url + "/reports/item-detail"
        self.item_rate_report = self.base_url + "/reports/item-rate-list"
        self.low_Stock_report = self.base_url + "/reports/low-stock-summary"
        self.stock_qty_report = self.base_url + "/reports/stock-quantity"
        self.expense_transactions_report = self.base_url + "/reports/expense-transaction"
        self.income_transactions_report = self.base_url + "/reports/income-transaction"
        self.expense_category_report = self.base_url + "/reports/expense-category"
        self.income_category_report = self.base_url + "/reports/income-category"
        self.cash_in_hand_report = self.base_url + "/reports/cash-in-hand-statement"
        self.bank_balance_report = self.base_url + "/reports/bank-statement"
        self.discount_report = self.base_url + "/reports/discount"
        self.sales_tax_report = self.base_url + "/reports/tax-sales"
        self.purchase_tax_report = self.base_url + "/reports/tax-purchase"

        self.staff_list = self.base_url + "/manage-staffs"

        self.import_parties = self.base_url + "/import-data/parties"
        self.import_items = self.base_url + "/import-data/items"

        self.general_settings = self.base_url + "/settings/general-settings"
        self.account_settings = self.base_url + "/settings/my-account"
        self.business_settings = self.base_url + "/settings/business-profile"
        self.subscription_settings = self.base_url + "/settings/subscription"
        self.parties_settings = self.base_url + "/settings/feature-settings/parties"
        self.item_settings = self.base_url + "/settings/feature-settings/inventory"
        self.transaction_settings = self.base_url + "/settings/feature-settings/transactions"
        self.invoice_settings = self.base_url + "/settings/feature-settings/invoice-print"

    def already_on_page(self, page_url):
        return self.driver.current_url == page_url
    
    def wait_until_text_visible(self, text, timeout=3):
        locator = (By.XPATH, f"//h2[contains(.,'{text}')]")
        conftest.waitForElement(self.driver, text=text, locator=locator, timeout=timeout, condition="visible")

    def navigate_to_dashboard(self):
        if self.already_on_page(self.base_url):
            self.wait_until_text_visible(text="Welcome")
            logging.info("Already on Dashboard, continuing...")
        else:
            self.driver.get(self.base_url)
            self.wait_until_text_visible(text="Welcome")
            self.driver.get(self.base_url)

    def navigate_to_parties(self):
        if self.already_on_page(self.parties_list):
            self.wait_until_text_visible(text="Parties")
            logging.info("Already on Parties List, continuing...")
        else:
            logging.info("Navigating to Parties List...")
            self.driver.get(self.parties_list)
            self.wait_until_text_visible(text="Parties")

    def navigate_to_item_list(self):
        if self.already_on_page(self.item_list):
            self.wait_until_text_visible(text="Items List")
            logging.info("Already on Item List, continuing...")
        else:
            logging.info("Navigating to Item List...")
            self.driver.get(self.item_list)
            self.wait_until_text_visible(text="Items List")
    
    def navigate_to_item_detail(self):
        if self.already_on_page(self.item_detail):
            self.wait_until_text_visible(text="Items")
            logging.info("Already on Item Detail, continuing...")
        else:
            logging.info("Navigating to Item Detail...")
            self.driver.get(self.item_detail)
            self.wait_until_text_visible(text="Items")
        
    def navigate_to_add_item(self):
        if self.already_on_page(self.add_item):
            self.wait_until_text_visible(text="Add New Item")
            logging.info("Already on Add Item, continuing...")
        else:
            logging.info("Navigating to Add Item...")
            self.driver.get(self.add_item)
            self.wait_until_text_visible(text="Add New Item")
    
    def navigate_to_sales_list(self):
        if self.already_on_page(self.sales_list):
            self.wait_until_text_visible(text="Sales Invoices")
            logging.info("Already on Sales List, continuing...")
        else:
            logging.info("Navigating to Sales List...")
            self.driver.get(self.sales_list)
            self.wait_until_text_visible(text="Sales Invoices")
    
    def navigate_to_add_sales(self):
        if self.already_on_page(self.add_sales):
            self.wait_until_text_visible(text="Create Sales Invoice")
            logging.info("Already on Add Sales, continuing...")
        else:
            logging.info("Navigating to Add Sales...")
            self.driver.get(self.add_sales)
            self.wait_until_text_visible(text="Create Sales Invoice")
    
    def navigate_to_payment_in_list(self):
        if self.already_on_page(self.payment_in_list):
            self.wait_until_text_visible(text="Payment In")
            logging.info("Already on Payment In List, continuing...")
        else:
            logging.info("Navigating to Payment In List...")
            self.driver.get(self.payment_in_list)
            self.wait_until_text_visible(text="Payment In")
    
    def navigate_to_quotation_list(self):
        if self.already_on_page(self.quotation_list):
            self.wait_until_text_visible(text="Quotations")
            logging.info("Already on Quotation List, continuing...")
        else:
            logging.info("Navigating to Quotation List...")
            self.driver.get(self.quotation_list)
            self.wait_until_text_visible(text="Quotations")
    
    def navigate_to_add_quotation(self):
        if self.already_on_page(self.add_quotation):
            self.wait_until_text_visible(text="Create Quotation")
            logging.info("Already on Add Quotation, continuing...")
        else:   
            logging.info("Navigating to Add Quotation...")
            self.driver.get(self.add_quotation)
            self.wait_until_text_visible(text="Create Quotation")

    def navigate_to_sales_return_list(self):
        if self.already_on_page(self.sales_return_list):
            self.wait_until_text_visible(text="Sales Return")
            logging.info("Already on Sales Return List, continuing...")
        else:
            logging.info("Navigating to Sales Return List...")
            self.driver.get(self.sales_return_list)
            self.wait_until_text_visible(text="Sales Return")
    
    def navigate_to_add_sales_return(self):
        if self.already_on_page(self.add_sales_return):
            self.wait_until_text_visible(text="Create Sales Return")    
            logging.info("Already on Add Sales Return, continuing...")
        else:
            logging.info("Navigating to Add Sales Return...")
            self.driver.get(self.add_sales_return)
            self.wait_until_text_visible(text="Create Sales Return")
    
    def navigate_to_purchase_list(self):
        if self.already_on_page(self.purchase_list):
            self.wait_until_text_visible(text="Purchase")
            logging.info("Already on Purchase List, continuing...")
        else:
            logging.info("Navigating to Purchase List...")
            self.driver.get(self.purchase_list)
            self.wait_until_text_visible(text="Purchase")   
    
    def navigate_to_add_purchase(self):
        if self.already_on_page(self.add_purchase):
            self.wait_until_text_visible(text="Create Purchase")
            logging.info("Already on Add Purchase, continuing...")
        else:
            logging.info("Navigating to Add Purchase...")
            self.driver.get(self.add_purchase)
            self.wait_until_text_visible(text="Create Purchase")
    
    def navigate_to_payment_out_list(self):
        if self.already_on_page(self.payment_out_list):
            self.wait_until_text_visible(text="Payment Out")
            logging.info("Already on Payment Out List, continuing...")
        else:
            logging.info("Navigating to Payment Out List...")
            self.driver.get(self.payment_out_list)
            self.wait_until_text_visible(text="Payment Out")
    
    def navigate_to_purchase_return_list(self):
        if self.already_on_page(self.purchase_return_list):
            self.wait_until_text_visible(text="Purchase Return")
            logging.info("Already on Purchase Return List, continuing...")
        else:
            logging.info("Navigating to Purchase Return List...")
            self.driver.get(self.purchase_return_list)
            self.wait_until_text_visible(text="Purchase Return")
    
    def navigate_to_add_purchase_return(self):
        if self.already_on_page(self.add_purchase_return):
            self.wait_until_text_visible(text="Create Purchase Return")
            logging.info("Already on Add Purchase Return, continuing...")
        else:
            logging.info("Navigating to Add Purchase Return...")
            self.driver.get(self.add_purchase_return)
            self.wait_until_text_visible(text="Create Purchase Return")
    
    def navigate_to_expenses_list(self):
        if self.already_on_page(self.expenses_list):
            self.wait_until_text_visible(text="Expenses")
            logging.info("Already on Expenses List, continuing...")
        else:
            logging.info("Navigating to Expenses List...")
            self.driver.get(self.expenses_list)
            self.wait_until_text_visible(text="Expenses")
    
    def navigate_to_income_list(self):
        if self.already_on_page(self.income_list):
            self.wait_until_text_visible(text="Income")
            logging.info("Already on Income List, continuing...")
        else:
            logging.info("Navigating to Income List...")
            self.driver.get(self.income_list)
            self.wait_until_text_visible(text="Income")
    
    def navigate_to_accounts_list(self):
        if self.already_on_page(self.accounts_list):
            self.wait_until_text_visible(text="Manage Accounts")
            logging.info("Already on Accounts List, continuing...")
        else:
            logging.info("Navigating to Accounts List...")
            self.driver.get(self.accounts_list)
            self.wait_until_text_visible(text="Manage Accounts")

    def navigate_to_reports_list(self):
        if self.already_on_page(self.reports_list):
            self.wait_until_text_visible(text="Reports")
            logging.info("Already on Reports List, continuing...")
        else:
            logging.info("Navigating to Reports List...")
            self.driver.get(self.reports_list)
            self.wait_until_text_visible(text="Reports")
    
    def navigate_to_sales_report(self):
        if self.already_on_page(self.sales_report):
            self.wait_until_text_visible(text="Sales Report")
            logging.info("Already on Sales Report, continuing...")    
        else:
            logging.info("Navigating to Sales Report...")
            self.driver.get(self.sales_report)
            self.wait_until_text_visible(text="Sales Report")
    
    def navigate_to_purchase_report(self):
        if self.already_on_page(self.purchase_report):
            self.wait_until_text_visible(text="Purchase Report")
            logging.info("Already on Purchase Report, continuing...")
        else:
            logging.info("Navigating to Purchase Report...")
            self.driver.get(self.purchase_report)
            self.wait_until_text_visible(text="Purchase Report")
    
    def navigate_to_sales_return_report(self):
        if self.already_on_page(self.sales_return_report):
            self.wait_until_text_visible(text="Sales Return Report")
            logging.info("Already on Sales Return Report, continuing...")
        else:
            logging.info("Navigating to Sales Return Report...")
            self.driver.get(self.sales_return_report)
            self.wait_until_text_visible(text="Sales Return Report")
    
    def navigate_to_purchase_return_report(self):
        if self.already_on_page(self.purchase_return_report):
            self.wait_until_text_visible(text="Purchase Return Report")
            logging.info("Already on Purchase Return Report, continuing...")
        else:
            logging.info("Navigating to Purchase Return Report...")
            self.driver.get(self.purchase_return_report)
            self.wait_until_text_visible(text="Purchase Return Report")
    
    def navigate_to_data_book_report(self):
        if self.already_on_page(self.data_book_report):
            self.wait_until_text_visible(text="Day Book")
            logging.info("Already on Data Book Report, continuing...")
        else:
            logging.info("Navigating to Data Book Report...")
            self.driver.get(self.data_book_report)
            self.wait_until_text_visible(text="Day Book")
    
    def navigate_to_all_transactions_report(self):
        if self.already_on_page(self.all_transactions_report):
            self.wait_until_text_visible(text="All Transactions")
            logging.info("Already on All Transactions Report, continuing...")
        else:
            logging.info("Navigating to All Transactions Report...")
            self.driver.get(self.all_transactions_report)
            self.wait_until_text_visible(text="All Transactions")
    
    def navigate_to_profit_loss_report(self):
        if self.already_on_page(self.profit_loss_report):
            self.wait_until_text_visible(text="Profit and Loss")
            logging.info("Already on Profit & Loss Report, continuing...")
        else:
            logging.info("Navigating to Profit & Loss Report...")
            self.driver.get(self.profit_loss_report)
            self.wait_until_text_visible(text="Profit and Loss")
    
    def navigate_to_party_statement_report(self):
        if self.already_on_page(self.party_statement_report):
            self.wait_until_text_visible(text="Party Statement")
            logging.info("Already on Party Statement Report, continuing...")
        else:
            logging.info("Navigating to Party Statement Report...")
            self.driver.get(self.party_statement_report)
            self.wait_until_text_visible(text="Party Statement")
    
    def navigate_to_all_parties_report(self):
        if self.already_on_page(self.all_parties_report):
            self.wait_until_text_visible(text="All Party")
            logging.info("Already on All Parties Report, continuing...")
        else:
            logging.info("Navigating to All Parties Report...")
            self.driver.get(self.all_parties_report)
            self.wait_until_text_visible(text="All Party")
    
    def navigate_to_item_details_report(self):
        if self.already_on_page(self.item_details_report):
            self.wait_until_text_visible(text="Item Detail")
            logging.info("Already on Item Details Report, continuing...")
        else:
            logging.info("Navigating to Item Details Report...")
            self.driver.get(self.item_details_report)
            self.wait_until_text_visible(text="Item Detail")
    
    def navigate_to_item_list_report(self):
        if self.already_on_page(self.item_rate_report):
            self.wait_until_text_visible(text="Item List")
            logging.info("Already on Item List Report, continuing...")
        else:
            logging.info("Navigating to Item List Report...")
            self.driver.get(self.item_rate_report)
            self.wait_until_text_visible(text="Item List")
    
    def navigate_to_low_stock_report(self):
        if self.already_on_page(self.low_Stock_report):
            self.wait_until_text_visible(text="Low Stock")
            logging.info("Already on Low Stock Report, continuing...")
        else:
            logging.info("Navigating to Low Stock Report...")
            self.driver.get(self.low_Stock_report)
            self.wait_until_text_visible(text="Low Stock")
    
    def navigate_to_stock_qty_report(self):
        if self.already_on_page(self.stock_qty_report):
            self.wait_until_text_visible(text="Stock Quantity")
            logging.info("Already on Stock Qty Report, continuing...")
        else:
            logging.info("Navigating to Stock Qty Report...")
            self.driver.get(self.stock_qty_report)
            self.wait_until_text_visible(text="Stock Quantity")

    def navigate_to_expense_transactions_report(self):
        if self.already_on_page(self.expense_transactions_report):
            self.wait_until_text_visible(text="Expense Transaction")
            logging.info("Already on Expense Transactions Report, continuing...")
        else:
            logging.info("Navigating to Expense Transactions Report...")
            self.driver.get(self.expense_transactions_report)
            self.wait_until_text_visible(text="Expense Transaction")
    
    def navigate_to_income_transactions_report(self):
        if self.already_on_page(self.income_transactions_report):
            self.wait_until_text_visible(text="Income Transaction")
            logging.info("Already on Income Transactions Report, continuing...")
        else:
            logging.info("Navigating to Income Transactions Report...")
            self.driver.get(self.income_transactions_report)
            self.wait_until_text_visible(text="Income Transaction")
    
    def navigate_to_expense_category_report(self):
        if self.already_on_page(self.expense_category_report):
            self.wait_until_text_visible(text="Expense Category")
            logging.info("Already on Expense Category Report, continuing...")
        else:
            logging.info("Navigating to Expense Category Report...")
            self.driver.get(self.expense_category_report)
            self.wait_until_text_visible(text="Expense Category")
    
    def navigate_to_income_category_report(self):
        if self.already_on_page(self.income_category_report):
            self.wait_until_text_visible(text="Income Category")
            logging.info("Already on Income Category Report, continuing...")
        else:
            logging.info("Navigating to Income Category Report...")
            self.driver.get(self.income_category_report)
            self.wait_until_text_visible(text="Income Category")
    
    def navigate_to_cash_in_hand_report(self):
        if self.already_on_page(self.cash_in_hand_report):
            self.wait_until_text_visible(text="Cash In Hand")
            logging.info("Already on Cash In Hand Report, continuing...")
        else:
            logging.info("Navigating to Cash In Hand Report...")
            self.driver.get(self.cash_in_hand_report)
            self.wait_until_text_visible(text="Cash In Hand")
    
    def navigate_to_bank_balance_report(self):
        if self.already_on_page(self.bank_balance_report):
            self.wait_until_text_visible(text="Bank Statement")
            logging.info("Already on Bank Balance Report, continuing...")
        else:
            logging.info("Navigating to Bank Balance Report...")
            self.driver.get(self.bank_balance_report)
            self.wait_until_text_visible(text="Bank Statement")

    def navigate_to_discount_report(self):
        if self.already_on_page(self.discount_report):
            self.wait_until_text_visible(text="Discount Report")
            logging.info("Already on Discount Report, continuing...")
        else:
            logging.info("Navigating to Discount Report...")
            self.driver.get(self.discount_report)
            self.wait_until_text_visible(text="Discount Report")
    
    def navigate_to_sales_tax_report(self):
        if self.already_on_page(self.sales_tax_report):
            self.wait_until_text_visible(text="Tax Sales")
            logging.info("Already on Sales Tax Report, continuing...")
        else:
            logging.info("Navigating to Sales Tax Report...")
            self.driver.get(self.sales_tax_report)
            self.wait_until_text_visible(text="Tax Sales")
    
    def navigate_to_purchase_tax_report(self):
        if self.already_on_page(self.purchase_tax_report):
            self.wait_until_text_visible(text="Tax Purchase")
            logging.info("Already on Purchase Tax Report, continuing...")
        else:
            logging.info("Navigating to Purchase Tax Report...")
            self.driver.get(self.purchase_tax_report)
            self.wait_until_text_visible(text="Tax Purchase")
    
    def navigate_to_staff_list(self):
        if self.already_on_page(self.staff_list):
            self.wait_until_text_visible(text="Manage Staffs")
            logging.info("Already on Staff List, continuing...")
        else:
            logging.info("Navigating to Staff List...")
            self.driver.get(self.staff_list)
            self.wait_until_text_visible(text="Manage Staffs")
    
    def navigate_to_import_parties(self):
        if self.already_on_page(self.import_parties):
            self.wait_until_text_visible(text="Import Parties")
            logging.info("Already on Import Parties, continuing...")
        else:
            logging.info("Navigating to Import Parties...")
            self.driver.get(self.import_parties)
            self.wait_until_text_visible(text="Import Parties")
    
    def navigate_to_import_items(self):
        if self.already_on_page(self.import_items):
            self.wait_until_text_visible(text="Import Items")
            logging.info("Already on Import Items, continuing...")
        else:
            logging.info("Navigating to Import Items...")
            self.driver.get(self.import_items)
            self.wait_until_text_visible(text="Import Items")
    
    def navigate_to_general_settings(self):
        if self.already_on_page(self.general_settings):
            self.wait_until_text_visible(text="General Settings")
            logging.info("Already on General Settings, continuing...")
        else:
            logging.info("Navigating to General Settings...")
            self.driver.get(self.general_settings)
            self.wait_until_text_visible(text="General Settings")
    
    def navigate_to_accounts_settings(self):
        if self.already_on_page(self.accounts_settings):
            self.wait_until_text_visible(text="My Account")
            logging.info("Already on Accounts Settings, continuing...")
        else:
            logging.info("Navigating to Accounts Settings...")
            self.driver.get(self.accounts_settings)
            self.wait_until_text_visible(text="My Account")
    
    def navigate_to_business_settings(self):
        if self.already_on_page(self.business_settings):
            self.wait_until_text_visible(text="Business Profile")
            logging.info("Already on Business Settings, continuing...")
        else:
            logging.info("Navigating to Business Settings...")
            self.driver.get(self.business_settings)
            self.wait_until_text_visible(text="Business Profile")
    
    def navigate_to_subscription_settings(self):
        if self.already_on_page(self.subscription_settings):
            self.wait_until_text_visible(text="Manage Subscription")
            logging.info("Already on Subscription Settings, continuing...")
        else:
            logging.info("Navigating to Subscription Settings...")
            self.driver.get(self.subscription_settings)
            self.wait_until_text_visible(text="Manage Subscription")    
    
    def navigate_to_parties_settings(self):
        if self.already_on_page(self.parties_settings):
            self.wait_until_text_visible(text="Parties Settings")
            logging.info("Already on Parties Settings, continuing...")
        else:
            logging.info("Navigating to Parties Settings...")
            self.driver.get(self.parties_settings)
            self.wait_until_text_visible(text="Parties Settings")
    
    def navigate_to_items_settings(self):
        if self.already_on_page(self.item_settings):
            self.wait_until_text_visible(text="Inventory Settings")
            logging.info("Already on Inventory Settings, continuing...")
        else:
            logging.info("Navigating to Inventory Settings...")
            self.driver.get(self.item_settings)
            self.wait_until_text_visible(text="Inventory Settings")
    
    def navigate_to_transaction_settings(self):
        if self.already_on_page(self.transaction_settings):
            self.wait_until_text_visible(text="Transaction Settings")
            logging.info("Already on Transaction Settings, continuing...")
        else:
            logging.info("Navigating to Transaction Settings...")
            self.driver.get(self.transaction_settings)
            self.wait_until_text_visible(text="Transaction Settings")
    
    def navigate_to_invoice_settings(self):
        if self.already_on_page(self.invoice_settings):
            self.wait_until_text_visible(text="Invoice Print Settings")
            logging.info("Already on Invoice Settings, continuing...")
        else:
            logging.info("Navigating to Invoice Settings...")
            self.driver.get(self.invoice_settings)
            self.wait_until_text_visible(text="Invoice Print Settings")