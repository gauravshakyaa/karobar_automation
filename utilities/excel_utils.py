import logging
import os
import openpyxl
import pandas as pd

def read_party_excel(filepath, sheetname="Party"):
    try:
        df = pd.read_excel(filepath, sheet_name=None)  # Load all sheets
        data = []
        print(pd.read_excel(filepath, sheet_name="Party"))
    except Exception as e:
        logging.error("Error while reading excel file: " + str(e))

    

read_party_excel("utilities//GuidedKarobarData.xlsx")
