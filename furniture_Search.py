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

    def FurnitureSearch(self):
        search = input("What furniture are you looking for today?: ")
        print(f"Searching for {search}...")

        found_items = []

        with open("Inventory/inventory.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("InventoryName") == search:
                    found_items.append(row)

    # pass search + results to next function
        self.displaySearchResults(search, found_items)


    def displaySearchResults(self, search, results):
        print(f"\nDisplaying search results for '{search}':")

        if not results:
            print("No items found.")
            return

        for item in results:
            print(f"- {item['InventoryName']} | {item['Status']} | {item['Quantity']} | ${item['Price']}")