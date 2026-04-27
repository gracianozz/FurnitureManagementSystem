# Artifact Name: staff_class.py
# Description: Implements Staff logic with dynamic login, full toolset, and input validation.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

import csv
import os

class Staff:
    def __init__(self, staff_id, fname=None, lname=None):
        self.staffID = staff_id
        self.fname = fname or "Unknown"
        self.lname = lname or ""
        if fname is None:
            self.load_staff_data()

    def load_staff_data(self):
        """Searches Staff/staff.csv for the ID and populates the object's attributes."""
        try:
            # Using utf-8-sig to handle invisible Excel encoding characters
            with open("Staff/staff.csv", "r", encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["staffID"].strip() == str(self.staffID):
                        self.fname = row["fName"].strip()
                        self.lname = row["lName"].strip()
                        break
        except FileNotFoundError:
            print("!!! SYSTEM ERROR: Staff/staff.csv database not found.")

    def display_staff_menu(self):
        """Main interface loop for Staff actions with input validation."""
        while True:
            print(f"\n--- Staff Portal: {self.fname} {self.lname} (ID: {self.staffID}) ---")
            print("1. Search Inventory")
            print("2. Report Damaged Item")
            print("3. Logout")
            
            choice = input("Select an option (1-3): ").strip()
            
            if choice == '1':
                self.search_inventory()
            elif choice == '2':
                self.report_damage()
            elif choice == '3':
                print(f"Logging out... Goodbye, {self.fname}!")
                break
            else:
                # Validation to handle any input other than 1, 2, or 3
                print("\n!!! ERROR: Invalid selection. Please enter 1, 2, or 3.")

    def search_inventory(self):
        """Allows Staff to look up furniture stock by SKU ID."""
        sku = input("\nEnter SKU to look up: ").strip().upper()
        try:
            with open("Inventory/inventory.csv", "r", encoding='utf-8-sig') as file:
                # Loading to a list for positional indexing to avoid header mismatch bugs
                reader = list(csv.reader(file))
                found = False
                for row in reader[1:]: # Skip headers
                    if len(row) > 1 and row[1].strip().upper() == sku:
                        print(f"\n[MATCH FOUND] Name: {row[2]} | Location: {row[3]} | Stock: {row[5]}")
                        found = True
                        break
                if not found:
                    print(f"!!! SKU '{sku}' not found in inventory.")
        except FileNotFoundError:
            print("!!! SYSTEM ERROR: Inventory/inventory.csv missing.")

    def report_damage(self):
        """Logs damage reports into a persistent CSV file."""
        sku = input("\nEnter SKU of damaged item: ").strip().upper()
        issue = input("Describe the damage/issue: ").strip()
        
        # Check if file exists to determine if we need a header
        file_exists = os.path.isfile("support_requests.csv")
        
        try:
            with open("support_requests.csv", "a", newline='') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["StaffID", "SKU", "Issue", "Status"])
                writer.writerow([self.staffID, sku, issue, "OPEN"])
            print(f"SUCCESS: Damage report for {sku} logged for Manager review.")
        except Exception as e:
            print(f"!!! FILE ERROR: Could not save report. {e}")

# Main execution block for testing
if __name__ == "__main__":
    print("--- Furniture Management System: Staff Login ---")
    user_id = input("Enter your Staff ID: ")
    current_staff = Staff(user_id)
    
    if current_staff.fname == "Unknown":
        print("!!! Access Denied: Staff ID not found in database.")
    else:
        current_staff.display_staff_menu()
        
