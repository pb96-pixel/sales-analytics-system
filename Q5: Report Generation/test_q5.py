import sys
import os

# --- Add project root to Python path ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

# --- Add specific folders to Python path ---
sys.path.append(os.path.join(PROJECT_ROOT, "Q2 Data File Handler & Preprocessing"))
sys.path.append(os.path.join(PROJECT_ROOT, "Q4 API Integration"))

# --- Now imports will work ---
from data_handler import read_sales_data, parse_transaction
from api_integration import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data
)
from report_generator import generate_sales_report


# --------- RUN PIPELINE ---------

# Read and parse sales data
lines = read_sales_data("../data/sales_data.txt")
transactions = []

for line in lines:
    txn = parse_transaction(line)
    if txn:
        transactions.append(txn)

# Fetch and map products
products = fetch_all_products()
product_map = create_product_mapping(products)

# Enrich transactions
enriched_transactions = enrich_sales_data(transactions, product_map)

# Generate report
generate_sales_report(transactions, enriched_transactions)
