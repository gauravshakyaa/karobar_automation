import logging
import pandas as pd

def read_party_excel(filepath, sheetname=None):
    try: 
        return pd.read_excel(filepath, sheet_name="Party Data")
    except Exception as e:
        logging.error("Error while reading excel file: " + str(e))



read_party_excel("utilities//GuidedKarobarData.xlsx")