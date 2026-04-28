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

    def PlaceCustomerOrder(self, customer):
        search = input("What furniture are you looking to order?: ")

        if not search:
            print("Please enter a valid item name.")
            return

        print(f"Searching for {search}...")
        found_items = []

        # Find items with matching names in csv
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

        # Loops until the customer is done searching for items
        try:
            again = input("Would you like to search again? (y/n): ")
        except ValueError:
                print("Invalid input. Please enter 'y' or 'n'.")
                return
        if again.lower() == "y":
            self.PlaceCustomerOrder(customer)
        
        elif again.lower() == "n" and found_items:
            total_available = sum(int(item.get("Quantity", 0)) for item in found_items) # Check if item is available
            if total_available == 0: 
                print("Sorry, this item is currently out of stock.")
            else:
                self.calculatePrice(search, found_items, customer.getCustomerID())
        
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return
        


    #Calculates total price, and progresses to checkout
    def calculatePrice(self, search, results, customer_id):

        try:
            amount = int(input(f"How many {search}s would you like to order?: "))
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")
            return
        sku_id = results[0]["SKU_ID"]

        with open(INVENTORY_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader: # Check if there is enough of item to meet customer demand
                if row.get("InventoryName") == search and int(row.get("Quantity", 0)) >= amount: 
                    total_price = amount * float(results[0]["Price"])
                    self.checkout(total_price, search, amount, customer_id, sku_id)
                    return

        print(f"Not enough stock to fulfill an order of {amount}.")

    # Print price, update inventory, save order
    def checkout(self, total_price, search, amount, customer_id, sku_id):
        print(f"Checkout complete. Total price: ${total_price:.2f}")
        self.updateInventory(search, amount)
        self.saveOrder(customer_id, sku_id)

    #Save the new order details to orders.csv
    def saveOrder(self, customer_id, sku_id):
        fieldnames = ["OrderID", "CustomerID", "SKU_ID", "OrderStatus", "PurchaseDate", "EstimatedDelivery"]
        rows = []

        with open(ORDERS_PATH, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        order_id = max(int(row["OrderID"]) for row in rows) + 1 if rows else 1001

        purchase_date = date.today()
        estimated_delivery = purchase_date + timedelta(days=7)

        # Append mode, applies each variable for an order object
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

    #Update the inventory after a customer places and order.
    def updateInventory(self, search, amount):
        rows = []
        fieldnames = []

        # Update csv based on the changes due to order
        with open(INVENTORY_PATH, "r") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                if row.get("InventoryName") == search:
                    new_qty = int(row["Quantity"]) - amount
                    row["Quantity"] = str(new_qty) # Lower quantity and update status
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

    #Process and logic of a manager placing an order
    def PlaceManagerOrder(self, manager):
        search = input("Enter furniture name to order: ")

        if not search:
            print("Please enter a valid item name.")
            return

        print(f"Searching for {search}...")
        found_items = []

        # Find matching item in inventory
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

        # Loop until manager is done adding items
        again = input("Would you like to search again? (y/n): ")
        if again.lower() == "y":
            self.PlaceManagerOrder(manager)
        elif again.lower() == "n" and found_items:
            if len(found_items) > 1:
                print("\nMultiple items found. Which one would you like to restock?") # Choose specific item if there are multiple matches
                for i, item in enumerate(found_items):
                    print(f"  {i + 1}. {item['InventoryName']} | Location: {item['Location']} | Qty: {item['Quantity']} (SKU: {item['SKU_ID']})")
                try:
                    choice = int(input("Enter the number (or 0 to cancel): "))
                    if choice == 0:
                        return
                    target_sku = found_items[choice - 1]["SKU_ID"]
                except (ValueError, IndexError):
                    print("Invalid selection. Operation cancelled.")
                    return
            else:
                target_sku = found_items[0]["SKU_ID"]

            # Input how much quantity should increase, with exception handling
            try:
                added = int(input(f"How many units would you like to add?: "))
            except ValueError:
                print("Please enter a valid quantity.")
                return
            if added <= 0:
                print("Please enter a quantity greater than 0.")
                return
            self.restockInventory(target_sku, added)

    #After making an order, restock the inventory based on the manager's input
    def restockInventory(self, target_sku, amount):
        rows = []
        fieldnames = []
        updated_name = ""

        # Update csv based on the changes due to order
        with open(INVENTORY_PATH, "r") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                if row.get("SKU_ID") == target_sku:
                    new_qty = int(row["Quantity"]) + amount
                    row["Quantity"] = str(new_qty) # Increase quantity and update status
                    updated_name = row["InventoryName"]
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

        print(f"Inventory updated. Added {amount} unit(s) of '{updated_name}'.")

