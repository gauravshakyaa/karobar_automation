import logging
import pandas as pd

def read_party_excel(filepath, sheetname=None):
    try: 
        df = pd.read_excel(filepath, sheet_name="Party Data")
        return df.to_dict(orient='records')
    except Exception as e:
        logging.error("Error while reading excel file: " + str(e))

def map_excel_keys(party_data):
    # Mapping Excel keys to method parameter names
    key_mapping = {
        "Party Name": "name",
        "Phone Number": "phone",
        "Opening Balance": "balance",
        "Balance Type": "balanceType",
        "Address": "address",
        "Email ID": "email",
        "PAN Number": "pan",
        "Type": "partyType"
    }
    return {key_mapping.get(k, k): v for k, v in party_data.items()}

party_details = read_party_excel("utilities//GuidedKarobarData.xlsx")
for index, party in enumerate(party_details):
    print(party_details)
