from api_integration import fetch_all_products, create_product_mapping

products = fetch_all_products()
product_map = create_product_mapping(products)

print("Total products fetched:", len(products))
print("Sample product:", list(product_map.items())[0])
