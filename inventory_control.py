import csv
from inventory import Inventory 
from furniture_Search import Furniture_Search

class inventory_control:
    def __init__(self, file_path=None):
        self.file_path = "Inventory/inventory.csv"
        self.headers = ["InventoryID", "SKU_ID", "InventoryName", "Location", "Status", "Quantity", "Price"]

    def _read_data(self):
        try:
            with open(self.file_path, "r", newline='') as file:
                return list(csv.DictReader(file, delimiter = '\t'))
        except FileNotFoundError:
            return []

    def _write_data(self, rows):
        with open(self.file_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames =self.headers, delimiter='\t')
            writer.writeheader()
            writer.writerows(rows)
    
    def get_next_ids(self):
        rows = self._read_data()

        # inventory id logic
        existing_ids = [int(r["InventoryID"]) for r in rows if r["InventoryID"].isdigit()]
        next_inv_id = str(max(existing_ids) + 1) if existing_ids else "2001"
        
        # sku id logic
        used_skus = {int(r["SKU_ID"].replace("SKU", "")) for r in rows if "SKU" in r["SKU_ID"]}
        next_sku_num = 101
        for i in range(101, 999):
            if i not in used_skus:
                next_sku_num = i
                break
        return next_inv_id, f"SKU{next_sku_num}"

    def add_furniture(self, name):
        inv_id, sku_id = self.get_next_ids()

        # initializes new furniture item
        new_item = Inventory(
            inventoryID = inv_id,
            name = name,
            skuID = sku_id,
            location = input("Location: "),
            quantity = int(input("Quantity: ")),
            status = "In Stock",
            price = input("Price: "))

        rows = self._read_data()
        rows.append(vars(new_item))
        self._write_data(rows)
        print(f"Success: Added {name} as {sku_id}")

    def remove_furniture(self, search_term):
        search_tool = Furniture_Search()
        matches = search_tool.FurnitureSearch(search_term)

        if not matches:
            print("Item not found.")
            return

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
        item = next((r for r in rows if r["SKU_ID"] == target_sku), None)
        
        print(f"Editing {item['InventoryName']}. Press Enter to skip fields.")
        item["InventoryName"] = input(f"Name [{item['InventoryName']}]: ") or item["InventoryName"]
        item["Location"] = input(f"Location [{item['Location']}]: ") or item["Location"]
        item["Quantity"] = input(f"Quantity [{item['Quantity']}]: ") or item["Quantity"]
        item["Status"] = input(f"Status [{item['Status']}]: ") or item["Status"]
        item["Price"] = input(f"Price [{item['Price']}]: ") or item["Price"]

        self._write_data(rows)
        print("Inventory updated.")
