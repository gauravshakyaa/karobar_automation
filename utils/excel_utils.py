import logging
import pandas as pd


party_key_mapping = {
        "Party Name": "name",
        "Phone Number": "phone",
        "Opening Balance": "balance",
        "Balance Type": "balanceType",
        "Address": "address",
        "Email ID": "email",
        "PAN Number": "pan",
        "Type": "partyType"
    }

item_key_mapping = {
    "Item Name": "itemName",
    "Item Category": "itemCategory",
    "Item Type": "itemType",
    "Opening Stock": "openingStock", 
    "Sales Price": "salesPrice",
    "Purchase Price": "purchasePrice", 
    "Primary Unit": "primary_unit",
    "Secondary Unit": "secondary_unit",
    "Conversion Rate": "conversionRate",
    "Item Code": "itemCode",
    "Remarks": "description",
    "Location": "location"
}

def read_excel(filepath, sheetname=None):
    try: 
        df = pd.read_excel(filepath, sheet_name=sheetname)
        df = df.replace({float('nan'): None})
        return df.to_dict(orient='records')
    except Exception as e:
        logging.error("Error while reading excel file: " + str(e))

def map_excel_keys(data, key_mapping):
    return {key_mapping.get(k, k): v for k, v in data.items()}

sales_details = read_excel("utils//GuidedKarobarData.xlsx", sheetname="Sales Data")
# mapped_item_data = [map_excel_keys(data=sale, key_mapping=item_key_mapping) for sale in sales_details]

print(sales_details[2])