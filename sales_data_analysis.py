""" 
Problem: Given a sales dataset in CSV format, the task is to analyze the data, 
calculate total sales for each product and category, identify the best-selling product, 
and store the results in a new CSV file.
Objectives:
*Read and process sales data from a CSV file.
*Calculate total sales for each product and sort them in descending order.
*Identify the best-selling product based on quantity.
*Compute total sales for each product category.
*Store the analyzed results in a new CSV file for easy access.

 """

import csv

# Read data from CSV file
file_path = "sales.csv"  
data = []

with open(file_path, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Price"] = int(row["Price"])  # Convert price to integer
        row["Quantity"] = int(row["Quantity"])  # Convert quantity to integer
        data.append(row)

# Step 1: Calculate Total Sales for Each Product
product_sales = {}
for row in data:
    product = row["Product"]
    total_price = row["Price"] * row["Quantity"]
    if product in product_sales:
        product_sales[product] += total_price
    else:
        product_sales[product] = total_price

# Step 2: Find the Best-Selling Product (By Quantity)
best_selling_product = max(data, key=lambda x: x["Quantity"])

# Step 3: Calculate Total Sales for Each Category
category_sales = {}
for row in data:
    category = row["Category"]
    total_price = row["Price"] * row["Quantity"]
    if category in category_sales:
        category_sales[category] += total_price
    else:
        category_sales[category] = total_price

# Step 4: Sort Products by Total Sales (Highest to Lowest)
sorted_product_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

# Step 5: Store Results in a New CSV File
output_file = "sales_summary.csv"

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write Headers
    writer.writerow(["Product", "Total Sales (Rupees)"])
    
    # Write Sorted Product Sales Data
    for product, sales in sorted_product_sales:
        writer.writerow([product, sales])
    
    writer.writerow([])  # Empty row for spacing
    
    # Write Best-Selling Product
    writer.writerow(["Best-Selling Product", best_selling_product["Product"]])
    writer.writerow(["Quantity Sold", best_selling_product["Quantity"]])
    
    writer.writerow([])  # Empty row for spacing

    # Write Category Sales
    writer.writerow(["Category", "Total Sales (Rupees)"])
    for category, sales in category_sales.items():
        writer.writerow([category, sales])

print(f"Results saved in {output_file}")
