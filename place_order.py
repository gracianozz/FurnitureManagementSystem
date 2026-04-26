# Artifact Name: place_order.py
# Description: Manages the customer checkout process and inventory updates.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

import csv
from datetime import date, timedelta

INVENTORY_PATH = "Inventory/inventory.csv"
ORDERS_PATH = "Orders/orders.csv"

class Place_Order:
    def __init__(self):
        pass

    def PlaceOrder(self, customer):
        search = input("What furniture are you looking to order?: ")

        if not search:
            print("Please enter a valid item name.")
            return

        print(f"Searching for {search}...")
        found_items = []

        with open(INVENTORY_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("InventoryName") == search:
                    found_items.append(row)

        if not found_items:
            print(f"No items found matching '{search}'.")
        else:
            print(f"\nFound {len(found_items)} item(s):")
            for item in found_items:
                print(f"  - {item.get('InventoryName')} | Price: ${float(item.get('Price', 0)):.2f} | Qty: {item.get('Quantity')}")

        again = input("Would you like to search again? (y/n): ")
        if again.lower() == "y":
            self.PlaceOrder(customer)
        elif again.lower() == "n" and found_items:
            self.calculatePrice(search, found_items, customer.getCustomerID())



    def calculatePrice(self, search, results, customer_id):
        amount = int(input(f"How many {search}s would you like to order?: "))
        sku_id = results[0]["SKU_ID"]

        with open(INVENTORY_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("InventoryName") == search and int(row.get("Quantity", 0)) >= amount:
                    total_price = amount * float(results[0]["Price"])
                    self.checkout(total_price, search, amount, customer_id, sku_id)
                    return

        print(f"Not enough stock to fulfill an order of {amount}.")

    def checkout(self, total_price, search, amount, customer_id, sku_id):
        print(f"Checkout complete. Total price: ${total_price:.2f}")
        self.updateInventory(search, amount)
        self.saveOrder(customer_id, sku_id)

    def saveOrder(self, customer_id, sku_id):
        fieldnames = ["OrderID", "CustomerID", "SKU_ID", "OrderStatus", "PurchaseDate", "EstimatedDelivery"]
        rows = []

        with open(ORDERS_PATH, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        order_id = max(int(row["OrderID"]) for row in rows) + 1 if rows else 1001

        purchase_date = date.today()
        estimated_delivery = purchase_date + timedelta(days=7)

        rows.append({
            "OrderID": order_id,
            "CustomerID": customer_id,
            "SKU_ID": sku_id,
            "OrderStatus": "Confirmed",
            "PurchaseDate": purchase_date.strftime("%Y-%m-%d"),
            "EstimatedDelivery": estimated_delivery.strftime("%Y-%m-%d")
        })

        with open(ORDERS_PATH, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Order #{order_id} saved! Estimated delivery: {estimated_delivery.strftime('%Y-%m-%d')}")

    def updateInventory(self, search, amount):
        rows = []
        fieldnames = []

        with open(INVENTORY_PATH, "r") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                if row.get("InventoryName") == search:
                    new_qty = int(row["Quantity"]) - amount
                    row["Quantity"] = str(new_qty)
                    if row["Status"] != "Reserved":
                        if new_qty == 0:
                            row["Status"] = "Out of Stock"
                        elif new_qty <= 5:
                            row["Status"] = "Low Stock"
                        else:
                            row["Status"] = "In Stock"
                rows.append(row)

        with open(INVENTORY_PATH, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
