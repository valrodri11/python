# System of categories for products with additional data
store = {
    "Electronics": [
        {"name": "Cell Phone X", "price": 300.0, "stock": 15},
        {"name": "Laptop Z", "price": 800.0, "stock": 5}
    ],
    "Clothing": [
        {"name": "T-Shirt", "price": 10.0, "stock": 20},
        {"name": "Pants", "price": 25.0, "stock": 10}
    ],
    "Home": [
        {"name": "Frying Pan", "price": 15.0, "stock": 8}
    ]
}

def get_stock(category, product):
    
    """ esta funcion obtiene el numero de productos de una categoria"""

    items = store.get(category)
    if items:
        for item in items:
            if item["name"] == product:
                return f"Available stock: {item['stock']}"
        return "Error: Product not found in this category."
    return "Error: The category does not exist."

def modify_stock(category, product, quantity):
    """ esta funcion modifica el numero de stocks"""
    items = store.get(category)
    if items:
        for item in items:
            if item["name"] == product:
                if item["stock"] + quantity >= 0:
                    item["stock"] += quantity
                    return f"The new stock of {product} is: {item['stock']}"
                else:
                    return "Error: Not enough stock to subtract that amount."
        return "Error: The product is not found in this category."
    return "Error: The category does not exist."

def show_products(category, sort_by):
    items = store.get(category)
    if not items:
        return "Error: The category does not exist."
    if sort_by not in ["name", "price"]:
        return "Error: You must sort by 'name' or 'price'."
    
    products = store[category][:] 
    sorted_products = []
    while products:
        smallest = products[0]
        for item in products:
            if item[sort_by] < smallest[sort_by]:
                smallest = item
            elif item[sort_by] == smallest[sort_by]:
                if item["name"] < smallest["name"]:
                    smallest = item 
        sorted_products.append(smallest)
        products.remove(smallest)
    
    for item in sorted_products:
        print(item)
    
    return sorted_products   

print("Categories available:")
for category in store.keys():
    print(f"- {category}")

category = input("Enter the category: ")
if category not in store:
    print("Error: The category does not exist.")
else:
    print(f"Products available in '{category}':")
    for product in store[category]:
        print(f"- {product}")
    product = input("Now, enter the product you want to search for: ")
    print(get_stock(category, product))


#quantity = int(input("Enter the quantity you want to add or subtract from stock: "))
#print(modify_stock(category, product, quantity))

# sort_by = input("Enter the criterion you want to sort by (name/price): ")
# show_products(category, sort_by)
