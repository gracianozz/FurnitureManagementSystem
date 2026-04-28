# Artifact Name: furniture_Search.py
# Description: Implements the search functionality for customers to browse the inventory.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

#This class will help the customer search for any furniture they want to buy.


import csv
from re import search


class Furniture_Search:
    def __init__(self):
        pass

    def FurnitureSearch(self, search_term=None):
        if search_term is None:
            search_term = input("What furniture are you looking for today?: ")
        print(f"Searching for {search_term}...")

        found_items = []

        # Check csv for the item they're searching for
        try:
            with open("Inventory/inventory.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row.get("InventoryName", "").lower() == search_term.lower():
                        found_items.append(row)
        except FileNotFoundError:  # Throw error if file couldn't be opened
            print("Error: Inventory file not found.")
            return []

        self.displaySearchResults(search_term, found_items)
        # Pass matches so other methods can use them
        return found_items

    # Displays search results in a user-friendly format
    def displaySearchResults(self, search, results):
        print(f"\nDisplaying search results for '{search}':")

        if not results:
            print("No items found.")
            return

        for item in results:
            print(f"- {item['InventoryName']} | {item['Status']} | {item['Quantity']} | ${item['Price']}")
