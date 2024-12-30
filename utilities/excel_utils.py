import logging
import os
import openpyxl

def read_party_excel(filepath, sheetname="Party"):
    try:
        workbook = openpyxl.load_workbook(filename=filepath)
        sheet = workbook[sheetname]
        max_row_count = sheet.max_row # Gets the maximum column number in the sheet
        cols = sheet.iter_rows(min_row=1, max_row=max_row_count, max_col=1)
        for col in cols:
            for cell in col:
                print(cell.value)
    except Exception as e:
        logging.error("Error while reading excel file: " + str(e))


read_party_excel("utilities//FreshData.xlsx", "FreshData")