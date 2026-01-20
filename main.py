from src.file_handler import load_and_clean_sales_data

file_path = "data/sales_data.txt"

total, invalid, valid = load_and_clean_sales_data(file_path)

print("Total records parsed:", total)
print("Invalid records removed:", invalid)
print("Valid records after cleaning:", len(valid))
