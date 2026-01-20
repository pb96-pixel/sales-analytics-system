from data_handler import read_sales_data, parse_transaction, validate_and_filter_transactions

file_path = "../data/sales_data.txt"

lines = read_sales_data(file_path)
transactions = [parse_transaction(line) for line in lines]

result = validate_and_filter_transactions(
    transactions,
    region="South",
    min_quantity=5
)

print("Total records:", result["total_records"])
print("Filtered records:", result["filtered_records"])