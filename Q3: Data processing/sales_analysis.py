def calculate_total_revenue(transactions):
    total_revenue = 0
    total_quantity = 0

    for txn in transactions:
        total_revenue += txn["Quantity"] * txn["UnitPrice"]
        total_quantity += txn["Quantity"]

    return {
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
        "total_transactions": len(transactions)
    }
def region_wise_sales(transactions):
    region_summary = {}

    for txn in transactions:
        region = txn["Region"]
        revenue = txn["Quantity"] * txn["UnitPrice"]

        if region not in region_summary:
            region_summary[region] = {
                "revenue": 0,
                "quantity": 0,
                "transactions": 0
            }

        region_summary[region]["revenue"] += revenue
        region_summary[region]["quantity"] += txn["Quantity"]
        region_summary[region]["transactions"] += 1

    return region_summary
def top_selling_products(transactions, n=3):
    product_summary = {}

    for txn in transactions:
        product = txn["ProductName"]
        revenue = txn["Quantity"] * txn["UnitPrice"]

        if product not in product_summary:
            product_summary[product] = {
                "total_quantity": 0,
                "total_revenue": 0
            }

        product_summary[product]["total_quantity"] += txn["Quantity"]
        product_summary[product]["total_revenue"] += revenue

    sorted_products = sorted(
        product_summary.items(),
        key=lambda x: x[1]["total_quantity"],
        reverse=True
    )

    return sorted_products[:n]
def customer_purchase_analysis(transactions):
    customer_summary = {}

    for txn in transactions:
        customer = txn["CustomerID"]
        amount = txn["Quantity"] * txn["UnitPrice"]

        if customer not in customer_summary:
            customer_summary[customer] = {
                "total_spent": 0,
                "purchases": 0
            }

        customer_summary[customer]["total_spent"] += amount
        customer_summary[customer]["purchases"] += 1

    for customer, data in customer_summary.items():
        if data["total_spent"] < 500:
            data["segment"] = "Low"
        elif data["total_spent"] < 2000:
            data["segment"] = "Medium"
        else:
            data["segment"] = "High"

    return customer_summary
def daily_sales_trend(transactions):
    daily_summary = {}

    for txn in transactions:
        date = txn["Date"]
        revenue = txn["Quantity"] * txn["UnitPrice"]

        if date not in daily_summary:
            daily_summary[date] = 0

        daily_summary[date] += revenue

    return dict(sorted(daily_summary.items()))
def peak_sales_day(transactions):
    daily_summary = daily_sales_trend(transactions)

    peak_day = max(daily_summary, key=daily_summary.get)
    return peak_day, daily_summary[peak_day]
def low_performing_products(transactions, threshold=5):
    product_summary = {}

    for txn in transactions:
        product = txn["ProductName"]

        if product not in product_summary:
            product_summary[product] = 0

        product_summary[product] += txn["Quantity"]

    low_performers = [
        product for product, qty in product_summary.items()
        if qty < threshold
    ]

    return low_performers
