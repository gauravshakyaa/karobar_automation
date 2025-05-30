import json
import logging
import re
import pandas as pd

KEY_MAPPINGS = {
    "party_key_mapping" : {
            "Party Name": "name",
            "Phone Number": "phone",     
            "Opening Balance": "balance",
            "Balance Type": "balanceType",
            "Address": "address",
            "Email ID": "email",
            "PAN Number": "pan",
            "Type": "partyType"
        },
    "item_key_mapping" : {
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
    },
    "item_adjustment_key_mapping" : {
        "Adjustment Type": "adjustment_type",
        "Item Name": "item_name",
        "Quantity to Add": "adjustment_qty",
        "Primary / Secondary": "secondary_unit",
        "Price": "rate"
    },
    "accounts_key_mapping" : {
        "Account Name": "account_name",
        "Account Type": "account_type"
    },
    "accounts_adjustment_key_mapping" : {
        "Txn Type": "adjustment_type",
        "Payment Account From": "from_account_name",
        "Payment Account To": "to_account_name",
        "Total Amount": "amount"
    },
    "payment_in_out_key_mapping": {
        "Receipt Number": "invoice_no",
        "Party Name": "party_name",
        "Amount": "total_amount",
        "Payment Mode": "payment_mode"
    },
    "income_expense_key_mapping": {
        "Number": "number",
        "Category": "category",
        "Total Amount": "total_amount",
        "Payment Mode": "payment_mode"
    }
}

def read_excel(filepath="utils//GuidedKarobarData.xlsx", sheet_name=None):
    try: 
        df = pd.read_excel(filepath, sheet_name=sheet_name)
        df = df.replace({float('nan'): None})
        return df.to_dict(orient='records')
    
    except Exception as e:
        logging.error("Error while reading excel file: " + str(e))

def map_excel_keys(key_mapping, sheet_name):
    excel_file_data = read_excel(sheet_name=sheet_name)
    mapped_data = []
    for data in excel_file_data:
        mapped_dict = {key_mapping.get(k.strip(), k.strip()): v for k, v in data.items()}
        mapped_data.append(mapped_dict)
    return mapped_data
 
def get_transaction_details_json(transaction_type=None):
    if transaction_type == "s":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheet_name="Sales Data")
    elif transaction_type == "p":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheet_name="Purchase Data")
    elif transaction_type == "sr":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheet_name="Sales Return Data")
    elif transaction_type == "pr":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheet_name="Purchase Return Data")
    elif transaction_type == "q":
        transaction_details = read_excel("utils//GuidedKarobarData.xlsx", sheet_name="Quotation Data")   
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

# print(map_excel_keys(KEY_MAPPINGS["party_key_mapping"], "Party Data"))
# print(map_excel_keys(KEY_MAPPINGS["payment_in_out_key_mapping"], "Payments In Data"))
# print(get_transaction_details_json(transaction_type='s'))

# excel = pd.read_excel("utils//GuidedKarobarData.xlsx", sheet_name="Data Overview")
# excel = excel.replace({float('nan'): None})
# print(excel.to_dict(orient='split'))

df = pd.read_excel("utils//GuidedKarobarData.xlsx", sheet_name="Data Overview", header=None, nrows=23)

df = df.replace({float('nan'): None})


sections = {}
current_section = None
current_headers = None
data_rows = []

def save_section():
    """Save the current section to the dictionary, processing appropriately."""
    if not current_section or not current_headers:
        return
    df_section = pd.DataFrame(data_rows)
    df_section.columns = current_headers[:len(df_section.columns)]
    sections[current_section] = df_section.dropna(how='all').to_dict(orient='records')

for idx, row in df.iterrows():
    values = row.tolist()

    # Detect section header (any containing "Overview")
    if any(isinstance(v, str) and "Overview" in v for v in values):
        save_section()
        current_section = next(v for v in values if isinstance(v, str) and "Overview" in v)
        current_headers = None
        data_rows = []
        continue

    # Identify headers for tables
    if current_section and not current_headers and any(isinstance(v, str) for v in values):
        current_headers = values
        continue

    # Append data rows under section
    if current_section and current_headers:
        data_rows.append(values)

# Save last section
save_section()

# Handle Dashboard (convert to key-value dictionary)
dashboard_dict = {}
for row in df.itertuples(index=False):
    if len(row) >= 3 and isinstance(row[1], str) and isinstance(row[2], (float, int)):
        dashboard_dict[row[1]] = row[2]
sections["Dashboard Data Overview"] = dashboard_dict

print(sections)