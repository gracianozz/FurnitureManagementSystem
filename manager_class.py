# Artifact Name: manager_class.py
# Description: Implements Manager logic including role-based inventory search.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

import csv

class Manager:
    _id_counter = 0
    
    def __init__(self, fname="", lname="", manager_id=None):
        Manager._id_counter += 1
        self.managerID = manager_id if manager_id is not None else Manager._id_counter
        self.fname = fname
        self.lname = lname

    def search_by_sku(self):
        """Allows manager to persistently search for inventory items by SKU ID."""
        while True:
            sku_to_find = input("\nEnter SKU to search (e.g., SKU222) or 'exit': ").strip().upper()
            
            if sku_to_find == 'EXIT':
                print("Exiting search menu...")
                break

            found = False
            try:
                # 'utf-8-sig' handles invisible Excel characters (BOM)
                with open("Inventory/inventory.csv", "r", encoding='utf-8-sig') as file:
                    reader = list(csv.reader(file))
                    
                    if len(reader) <= 1:
                        print("!!! ERROR: Inventory database is currently empty.")
                        break

                    # Start from index 1 to skip the header row
                    for row in reader[1:]:
                        # row[1] = SKU_ID, row[2] = Name, row[3] = Loc, row[5] = Qty, row[6] = Price
                        if len(row) > 1 and row[1].strip().upper() == sku_to_find:
                            print(f"\n[MATCH FOUND]: {row[2]}")
                            print(f"Location: {row[3]} | Stock: {row[5]} | Price: ${row[6]}")
                            found = True
                            break 
                    
                    if not found:
                        print(f"!!! ERROR: SKU '{sku_to_find}' not found in database. Please try again.")
            except FileNotFoundError:
                print("!!! ERROR: System cannot find 'Inventory/inventory.csv'. Check file path.")
                break

# Local testing block
if __name__ == "__main__":
    current_manager = Manager("Ashfaqh", "Rahmath")
    print(f"--- Welcome Manager {current_manager.fname} (ID: {current_manager.managerID}) ---")
    current_manager.search_by_sku()