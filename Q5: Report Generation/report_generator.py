from datetime import datetime


def generate_sales_report(transactions, enriched_transactions, output_file="sales_report.txt"):
    with open(output_file, "w", encoding="utf-8") as file:

        # ================= HEADER =================
        file.write("SALES ANALYTICS REPORT\n")
        file.write("=" * 50 + "\n")
        file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Records Processed: {len(transactions)}\n\n")

        # ================= OVERALL SUMMARY =================
        total_revenue = sum(txn["Quantity"] * txn["UnitPrice"] for txn in transactions)
        total_transactions = len(transactions)
        avg_order_value = total_revenue / total_transactions if total_transactions else 0

        dates = [txn["Date"] for txn in transactions]
        date_range = f"{min(dates)} to {max(dates)}" if dates else "N/A"

        file.write("OVERALL SUMMARY\n")
        file.write("-" * 50 + "\n")
        file.write(f"Total Revenue: {total_revenue:,.2f}\n")
        file.write(f"Total Transactions: {total_transactions}\n")
        file.write(f"Average Order Value: {avg_order_value:,.2f}\n")
        file.write(f"Date Range: {date_range}\n\n")

        # ================= REGION-WISE PERFORMANCE =================
        region_summary = {}
        for txn in transactions:
            region = txn["Region"]
            revenue = txn["Quantity"] * txn["UnitPrice"]

            if region not in region_summary:
                region_summary[region] = {"revenue": 0, "count": 0}

            region_summary[region]["revenue"] += revenue
            region_summary[region]["count"] += 1

        file.write("REGION-WISE PERFORMANCE\n")
        file.write("-" * 50 + "\n")
        file.write("Region | Sales | % of Total | Transactions\n")

        for region, data in region_summary.items():
            percent = (data["revenue"] / total_revenue) * 100 if total_revenue else 0
            file.write(
                f"{region} | {data['revenue']:,.2f} | {percent:.2f}% | {data['count']}\n"
            )
        file.write("\n")

        # ================= TOP PRODUCTS =================
        product_summary = {}
        for txn in transactions:
            product = txn["ProductName"]
            revenue = txn["Quantity"] * txn["UnitPrice"]

            if product not in product_summary:
                product_summary[product] = {"qty": 0, "revenue": 0}

            product_summary[product]["qty"] += txn["Quantity"]
            product_summary[product]["revenue"] += revenue

        top_products = sorted(
            product_summary.items(),
            key=lambda x: x[1]["qty"],
            reverse=True
        )[:5]

        file.write("TOP 5 PRODUCTS\n")
        file.write("-" * 50 + "\n")
        file.write("Rank | Product | Quantity | Revenue\n")

        for i, (product, data) in enumerate(top_products, start=1):
            file.write(
                f"{i} | {product} | {data['qty']} | {data['revenue']:,.2f}\n"
            )
        file.write("\n")

        # ================= DAILY SALES TREND =================
        daily_summary = {}
        for txn in transactions:
            date = txn["Date"]
            revenue = txn["Quantity"] * txn["UnitPrice"]

            daily_summary[date] = daily_summary.get(date, 0) + revenue

        file.write("DAILY SALES TREND\n")
        file.write("-" * 50 + "\n")
        file.write("Date | Revenue\n")

        for date, revenue in sorted(daily_summary.items()):
            file.write(f"{date} | {revenue:,.2f}\n")
        file.write("\n")

        # ================= API ENRICHMENT SUMMARY =================
        enriched_count = len(enriched_transactions)
        missing_products = [
            txn for txn in enriched_transactions
            if txn.get("ProductName") == "Unknown"
        ]

        file.write("API ENRICHMENT SUMMARY\n")
        file.write("-" * 50 + "\n")
        file.write(f"Total records enriched: {enriched_count}\n")
        file.write(f"Records not enriched: {len(missing_products)}\n")

    print(f"Report generated successfully: {output_file}")
