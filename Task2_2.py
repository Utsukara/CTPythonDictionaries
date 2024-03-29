# Task 2: E-commerce Product Search Feature
# Put your data handling and string manipulation skills to the test by creating a product search feature for an e-commerce platform.

# Problem Statement:
# Create a system that:

# Holds a dictionary of products where each product has attributes like name, category, and price.
# Implement a search function that allows searching for products by name, returning a list of matching products (case-insensitive search).
# Handle cases where no matches are found.
# Example product dictionary:

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

def search_item(item_name):
    for prododuct_id, product_info in products.items():
        if product_info["name"].lower() == item_name.lower():
                print(f"""ID: {prododuct_id}
Product: {product_info["name"]}
Category: {product_info["category"]}
Price: ${product_info["price"]}\n""")
                return None
    
    print(f"Item not found.\n")
    return None

search_item("laptop")
search_item("computer")