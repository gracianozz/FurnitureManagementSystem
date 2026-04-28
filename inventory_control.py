import csv
from furniture_Search import Furniture_Search

class inventory_control:
    def __init__(self, file_path=None):
        self.file_path = "Inventory/inventory.csv"
        self.headers = ["InventoryID", "SKU_ID", "InventoryName", "Location", "Status", "Quantity", "Price"]

    # Method for reading data, for code brevity
    def _read_data(self):
        try:
            with open(self.file_path, "r", newline='') as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            return []

    # Method for writing data, for code brevity
    def _write_data(self, rows):
        with open(self.file_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(rows)

    # Logic for assigning InventoryID and skuID
    def get_next_ids(self):
        rows = [r for r in self._read_data() if r["InventoryID"].isdigit()]

        existing_ids = [int(r["InventoryID"]) for r in rows]
        next_inv_id = str(max(existing_ids) + 1) if existing_ids else "2001" # ranges from 2001 to 9999

        used_skus = {int(r["SKU_ID"][3:]) for r in rows if r["SKU_ID"].startswith("SKU") and r["SKU_ID"][3:].isdigit()}
        next_sku_num = 101
        for i in range(101, 999): # ranges from 101 to 999
            if i not in used_skus:
                next_sku_num = i
                break
        return next_inv_id, f"SKU{next_sku_num}"

    def add_furniture(self, name):
        inv_id, sku_id = self.get_next_ids()
        # User inputs Location, Quantity, and Price
        # --- Location (String) ---
        while True:
            location = input("Location: ").strip()
            if location and not location.isdigit(): # Ensures it's not empty and not just numbers
                break
            print("Invalid input. Please enter a valid location name.")
        
        # --- Quantity (Integer) ---
        while True:
            try:
                quantity = int(input("Quantity: "))
                break # Exit loop if conversion to int succeeds
            except ValueError:
                print("Invalid input. Please enter a whole number (integer).")
        
        # --- Price (Float) ---
        while True:
            try:
                price = float(input("Price: "))
                break # Exit loop if conversion to float succeeds
            except ValueError:
                print("Invalid input. Please enter a decimal number (float).")

        new_row = {
            "InventoryID": inv_id,
            "SKU_ID": sku_id,
            "InventoryName": name,
            "Location": location,
            "Status": "Out of Stock" if quantity == 0 else "Low Stock" if quantity <= 5 else "In Stock",
            "Quantity": quantity,
            "Price": price
        }

        rows = self._read_data()
        rows.append(new_row)
        self._write_data(rows)

        print(f"Success: Added {name} as {sku_id}")

    def remove_furniture(self, search_term):
        search_tool = Furniture_Search()
        matches = search_tool.FurnitureSearch(search_term)

        if not matches:
            return

        # Choose specific item if there are multiple matches
        if len(matches) > 1:
            print("\nMultiple items found. Which one would you like to remove?")
            for i, item in enumerate(matches):
                print(f"{i + 1}. {item['InventoryName']} | {item['Location']} (SKU: {item['SKU_ID']})")
            
            try:
                choice = int(input("\nEnter the number to remove (or 0 to cancel): "))
                if choice == 0: return
                
                # Get specific sku ID, -1 to adjust for 0
                target_sku = matches[choice - 1]["SKU_ID"]
            except (ValueError, IndexError):
                print("Invalid selection. Operation cancelled.")
                return
        else:
            # Only one match found, target it directly
            target_sku = matches[0]["SKU_ID"]

        rows = self._read_data()
        rows = [r for r in rows if r["SKU_ID"] != target_sku]
        self._write_data(rows)
        print(f"Item {target_sku} removed successfully.")

    def edit_furniture(self, search_term):
        search_tool = Furniture_Search()
        matches = search_tool.FurnitureSearch(search_term)

        if not matches:
            print("Item not found.")
            return

        # Choose specific item if there are multiple matches
        if len(matches) > 1:
            print("\nMultiple items found. Which one would you like to edit?")
            for i, item in enumerate(matches):
                print(f"{i + 1}. {item['InventoryName']} | {item['Location']} (SKU: {item['SKU_ID']})")
            
            try:
                choice = int(input("\nEnter the number to edit (or 0 to cancel): "))
                if choice == 0: return
                
                # Get specific sku ID, -1 to adjust for 0
                target_sku = matches[choice - 1]["SKU_ID"]
            except (ValueError, IndexError):
                print("Invalid selection. Operation cancelled.")
                return
        else:
            # Only one match found, target it directly
            target_sku = matches[0]["SKU_ID"]

        rows = self._read_data()
        item = next((r for r in rows if r["SKU_ID"] == target_sku), None)

        if item is None:
            print("Item not found in inventory.")
            return

        # User inputs all edit-able variables of an object, Enter to leave them the same
        print(f"Editing {item['InventoryName']}. Press Enter to skip fields.")
        item["InventoryName"] = input(f"Name [{item['InventoryName']}]: ") or item["InventoryName"]
        item["Location"] = input(f"Location [{item['Location']}]: ") or item["Location"]
        item["Quantity"] = input(f"Quantity [{item['Quantity']}]: ") or item["Quantity"]
        item["Price"] = input(f"Price [{item['Price']}]: ") or item["Price"]

        qty = int(item["Quantity"]) if str(item["Quantity"]).isdigit() else 0
        if item["Status"] != "Reserved":
            if qty == 0:
                item["Status"] = "Out of Stock"
            elif qty <= 5:
                item["Status"] = "Low Stock"
            else:
                item["Status"] = "In Stock"

        self._write_data(rows)
        print(f"Inventory updated. Status set to '{item['Status']}' based on quantity {item['Quantity']}.")
