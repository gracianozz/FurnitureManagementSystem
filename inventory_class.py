# Artifact Name: inventory_class.py
# Description: Entity class representing individual furniture items and their attributes.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026


class Inventory():
    
    def __init__(self, inventoryID, name, skuID, location, quantity, status, price):
        self.inventoryID = inventoryID
        self.name = name
        self.skuID = skuID 
        self.location = location
        self.quantity = quantity
        self.status = status
        self.price = price




        
