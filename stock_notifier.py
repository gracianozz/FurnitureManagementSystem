import csv

INVENTORY_PATH = "Inventory/inventory.csv"
NOTIS_PATH = "stockNotifications/stockNotis.csv"

class stock:
    def __init__(self):
        pass

    def check_stock(self):
        low_stock_items = []

        with open(INVENTORY_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("Status") == "Low Stock":
                    low_stock_items.append({
                        "InventoryID": row["InventoryID"],
                        "SKU_ID": row["SKU_ID"],
                        "InventoryName": row["InventoryName"],
                        "Message": f"{row['InventoryName']} is in low stock"
                    })

        with open(NOTIS_PATH, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["InventoryID", "SKU_ID", "InventoryName", "Message"])
            writer.writeheader()
            writer.writerows(low_stock_items)

        print(f"{len(low_stock_items)} low stock item(s) found.")
        self.displayStockAlerts()

    def manage_inventory(self):
        print("Managing inventory")

    def displayStockAlerts(self):
        print("\n===============================================")
        print("Stock Alerts:")
        print("===============================================")

        with open(NOTIS_PATH, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        if not rows:
            print("No low stock alerts.")
            return

        for row in rows:
            print(f"[ID: {row['InventoryID']}] [{row['SKU_ID']}] {row['Message']}")
