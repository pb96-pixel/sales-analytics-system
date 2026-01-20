import sys
import os

# ---------------- PATH SETUP ----------------
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)

sys.path.append(os.path.join(PROJECT_ROOT, "src"))
sys.path.append(os.path.join(PROJECT_ROOT, "Q2 Data File Handler & Preprocessing"))
sys.path.append(os.path.join(PROJECT_ROOT, "Q3 Data Processing"))
sys.path.append(os.path.join(PROJECT_ROOT, "Q4 API Integration"))
sys.path.append(os.path.join(PROJECT_ROOT, "Q5 Report Generation"))

# ---------------- IMPORTS ----------------
from file_handler import load_and_clean_sales_data
from data_handler import read_sales_data, parse_transaction
from sales_analysis import (
    calculate_total_revenue,
    region_wise_sales,
    top_selling_products,
    customer_purchase_analysis
)
from api_integration import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data,
    save_enriched_data_to_file
)
from report_generator import generate_sales_report


# ---------------- MAIN FUNCTION ----------------
def main():
    try:
        print("=" * 40)
        print("SALES ANALYTICS SYSTEM")
        print("=" * 40)

        # 1. Read raw data
        print("\n[1/10] Reading sales data...")
        lines = read_sales_data("data/sales_data.txt")
        print(f"✓ Successfully read {len(lines)} records")

        # 2. Parse & clean
        print("\n[2/10] Parsing and cleaning data...")
        transactions = []
        for line in lines:
            txn = parse_transaction(line)
            if txn:
                transactions.append(txn)

        print(f"✓ Valid records: {len(transactions)}")

        # 3. Filter options
        print("\n[3/10] Filter Options Available:")
        print("Regions: North, South, East, West")
        print("Amount Range: e.g. 100-1000")

        region_filter = input("Enter region to filter (or press Enter to skip): ").strip()
        amount_filter = input("Enter amount range (min-max) or press Enter to skip: ").strip()

        # 4. Apply filters
        print("\n[4/10] Validating filters...")
        filtered = transactions

        if region_filter:
            filtered = [t for t in filtered if t["Region"].lower() == region_filter.lower()]

        if amount_filter:
            min_amt, max_amt = map(float, amount_filter.split("-"))
            filtered = [
                t for t in filtered
                if min_amt <= t["Quantity"] * t["UnitPrice"] <= max_amt
            ]

        print(f"✓ Records after filtering: {len(filtered)}")

        # 5. Analytics
        print("\n[5/10] Analyzing sales data...")
        total_revenue = calculate_total_revenue(filtered)
        region_stats = region_wise_sales(filtered)
        top_products = top_selling_products(filtered)
        customer_stats = customer_purchase_analysis(filtered)
        print("✓ Analysis complete")

        # 6. API fetch
        print("\n[6/10] Fetching product data from API...")
        products = fetch_all_products()
        product_map = create_product_mapping(products)
        print("✓ Product data fetched")

        # 7. Enrich data
        print("\n[7/10] Enriching sales data...")
        enriched_transactions = enrich_sales_data(filtered, product_map)
        print("✓ Enrichment complete")

        # 8. Save enriched data
        print("\n[8/10] Saving enriched sales data...")
        save_enriched_data_to_file(enriched_transactions)
        print("✓ Saved to enriched_sales_data.txt")

        # 9. Generate report
        print("\n[9/10] Generating sales report...")
        generate_sales_report(filtered, enriched_transactions)
        print("✓ Report saved to sales_report.txt")

        # 10. Done
        print("\n[10/10] Process Complete!")
        print("=" * 40)

    except Exception as e:
        print("\n❌ ERROR OCCURRED")
        print(str(e))
        print("Please check inputs or file paths.")


# ---------------- RUN ----------------
if __name__ == "__main__":
    main()
