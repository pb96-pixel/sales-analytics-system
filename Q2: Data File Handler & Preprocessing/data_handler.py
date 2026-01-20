def read_sales_data(file_path):
    """
    Reads sales data from a file with encoding handling.
    Returns a list of raw data lines (excluding header).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Remove header and empty lines
        data_lines = []
        for line in lines[1:]:
            line = line.strip()
            if line:
                data_lines.append(line)

        return data_lines

    except UnicodeDecodeError:
        print("Encoding error while reading the file.")
        return []
def parse_transaction(line):
    """
    Parses a single sales record line into a dictionary.
    """
    parts = line.split("|")

    if len(parts) != 8:
        return None

    try:
        transaction = {
            "TransactionID": parts[0],
            "Date": parts[1],
            "ProductID": parts[2],
            "ProductName": parts[3],
            "Quantity": int(parts[4].strip()),
            "UnitPrice": float(parts[5].replace(",", "").strip()),
            "CustomerID": parts[6],
            "Region": parts[7]
        }

        return transaction

    except:
        return None
def validate_and_filter_transactions(transactions, region=None, min_quantity=1, start_date=None, end_date=None):
    """
    Filters transactions based on provided criteria.
    """
    filtered = []

    for txn in transactions:
        if txn is None:
            continue

        if region and txn["Region"] != region:
            continue

        if txn["Quantity"] < min_quantity:
            continue

        if start_date and txn["Date"] < start_date:
            continue

        if end_date and txn["Date"] > end_date:
            continue

        filtered.append(txn)

    return {
        "total_records": len(transactions),
        "filtered_records": len(filtered),
        "data": filtered
    }