# Define the inventory data for three warehouses
warehouse1 = [("product1", 50), ("product2", 30), ("product3", 20)]
warehouse2 = [("product4", 40), ("product2", 20), ("product5", 60)]
warehouse3 = [("product6", 70), ("product3", 10), ("product7", 25)]

# Prompt the user to enter a product identifier
product_id = input("Enter product identifier: ")

# Initialize total quantity available
total_quantity = 0
found = False

# Iterate over each warehouse's inventory to check for the product
for warehouse in [warehouse1, warehouse2, warehouse3]:
    for item in warehouse:
        if item[0] == product_id:
            total_quantity += item[1]
            found = True
            break  # Break the inner loop if product is found in current warehouse

# Check if product is available and display the total quantity available
if found:
    print(f"Total quantity of product {product_id}: {total_quantity}")
else:
    print("Product is out of stock.")

