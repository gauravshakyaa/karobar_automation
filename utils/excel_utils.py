import json
import logging
import re
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

def get_transaction_details_json(transaction_type=None):
    if transaction_type == "s":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheetname="Sales Data")
    elif transaction_type == "p":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheetname="Purchase Data")
    elif transaction_type == "sr":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheetname="Sales Return Data")
    elif transaction_type == "pr":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheetname="Purchase Return Data")
    elif transaction_type == "q":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheetname="Quotation Data")   
    else:
        logging.error("Invalid transaction type provided")
        return None
    structured_sales = []
    for row in transaction_details:
        structured_billing_items = []

        billing_text = (row.get("Billing Details") or "").strip()   # Get value safely, stripping whitespace
        
        # Regex to extract item details
        item_pattern = r"Item\s*(\d+):\s*([\d.]*)\s*([\w]*)\s*@\s*Rs[.\s]*([\d.]*)(?:\s*with\s*([\d.]*)%\s*Discount)?"

        # Regex to capture overall discount, tax, and charges
        discount_percent_pattern = r"Overall Discount[:\s]+([\d.]*)%"
        discount_amount_pattern = r"Overall Discount[:\s]+Rs\.\s*([\d.]+)"
        tax_pattern = r"Tax[:\s]+([\d.]*)%"
        charge_pattern = r"Charge\s\d+[:\s]+Rs[.\s]*([\d.]*)"

        matches = re.findall(item_pattern, billing_text)

        overall_discount_percent = re.search(discount_percent_pattern, billing_text)
        overall_discount_amount = re.search(discount_amount_pattern, billing_text)
        tax = re.search(tax_pattern, billing_text)
        charges = re.findall(charge_pattern, billing_text)
        
        for match in matches:
            item = {
                "item_name": f"Item {match[0]}",
                "quantity": float(match[1]) if match[1] else None, 
                "secondary_unit": match[2] if match[2] else None,  
                "rate": float(match[3]) if match[3] else None,
                "item_discount_percent": float(match[4]) if match[4] else None
            }
           
            structured_billing_items.append(item)

        structured_row = {
            "invoice_number": row.get("Invoice No.", None),
            "party_name": row.get("Bill To:").strip(),
            "Billing Details": structured_billing_items,
            "overall_discount_percent":  float(overall_discount_percent.group(1)) if overall_discount_percent else None,
            "overall_discount_amount": float(overall_discount_amount.group(1)) if overall_discount_amount else None,
            "tax": float(tax.group(1)) if tax and tax.group(1) else None,
            "charge_amount": [float(charge) for charge in (charges or []) if charge] if charges else None,
            "total_amount": float(row["Total Amount"]) if row.get("Total Amount") not in [None, ""] else None,
            "used_amount": (
                float(row["Received Amount"]) if row.get("Received Amount") not in [None, ""] 
                else float(row["Paid Amount"]) if row.get("Paid Amount") not in [None, ""] 
                else None
            ),
            "payment_mode": row.get("Payment Mode", "").strip(),
        }

        structured_sales.append(structured_row)

    return json.dumps(structured_sales)


#####  This is for test purpose only #####
transaction_json_data = json.loads(get_transaction_details_json(transaction_type="q"))
for transaction in transaction_json_data:
    invoice_number = transaction.get("invoice_number")
    party_name = transaction.get("party_name")
    billing_details = transaction.get("Billing Details", [])
    total_amount = transaction.get("total_amount")
    used_amount = transaction.get("used_amount")
    payment_mode = transaction.get("payment_mode")
    overall_discount_percent = transaction.get("overall_discount_percent")
    overall_discount_amount = transaction.get("overall_discount_amount")
    tax = bool(transaction.get("tax"))
    charge_amount = transaction.get("charge_amount") if transaction.get("charge_amount") else None
    for index, item in enumerate(billing_details, start=1):
        item_details = {
            "index": index,
            "item_name": item.get("item_name"),
            "quantity": item.get("quantity"),
            "secondary_unit": item.get("secondary_unit"),
            "rate": item.get("rate"),
            "discount_percent": item.get("item_discount_percent") if item.get("item_discount_percent") is not None else item.get("discount_amount"),
        }
    print(transaction)
    print()

