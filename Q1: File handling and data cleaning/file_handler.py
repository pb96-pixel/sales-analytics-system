import csv

def load_and_clean_sales_data(file_path):
    total_records = 0
    invalid_records = 0
    valid_records = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="|")
        header = next(reader)  # skip header

        for row in reader:
            # Ignore completely empty lines
            if not row or len(row) < 8:
                continue

            total_records += 1

            quantity_raw = row[4].strip()
            price_raw = row[5].replace(",", "").strip()

            # Missing values → invalid
            if quantity_raw == "" or price_raw == "":
                invalid_records += 1
                continue

            try:
                quantity = int(quantity_raw)
                price = float(price_raw)

                # Assignment rule
                if quantity <= 0 or price <= 0:
                    invalid_records += 1
                else:
                    valid_records.append(row)

            except:
                invalid_records += 1

    return total_records, invalid_records, valid_records
