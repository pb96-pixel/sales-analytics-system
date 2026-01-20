import requests

BASE_URL = "https://dummyjson.com/products"
def fetch_all_products():
    """
    Fetch all products from DummyJSON API.
    Returns a list of product dictionaries.
    """
    try:
        response = requests.get(BASE_URL, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return data.get("products", [])
        else:
            print("API Error:", response.status_code)
            return []

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return []
def create_product_mapping(products):
    """
    Create mapping of product_id to product details.
    """
    product_map = {}

    for product in products:
        product_map[product["id"]] = {
            "title": product["title"],
            "category": product["category"],
            "price": product["price"],
            "rating": product["rating"]
        }

    return product_map
def enrich_sales_data(transactions, product_mapping):
    """
    Enrich sales transactions with product details.
    """
    enriched_data = []

    for txn in transactions:
        product_id = txn.get("ProductID")

        product_info = product_mapping.get(product_id, {
            "title": "Unknown",
            "category": "Unknown",
            "price": 0,
            "rating": 0
        })

        enriched_txn = txn.copy()
        enriched_txn.update({
            "ProductName": product_info["title"],
            "Category": product_info["category"],
            "Rating": product_info["rating"]
        })

        enriched_data.append(enriched_txn)

    return enriched_data
def save_enriched_data_to_file(enriched_data, file_path="enriched_sales_data.txt"):
    """
    Save enriched sales data to a text file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        header = "TransactionID|Date|ProductID|ProductName|Category|Quantity|UnitPrice|CustomerID|Region|Rating\n"
        file.write(header)

        for txn in enriched_data:
            line = (
                f"{txn.get('TransactionID')}|"
                f"{txn.get('Date')}|"
                f"{txn.get('ProductID')}|"
                f"{txn.get('ProductName')}|"
                f"{txn.get('Category')}|"
                f"{txn.get('Quantity')}|"
                f"{txn.get('UnitPrice')}|"
                f"{txn.get('CustomerID')}|"
                f"{txn.get('Region')}|"
                f"{txn.get('Rating')}\n"
            )
            file.write(line)
