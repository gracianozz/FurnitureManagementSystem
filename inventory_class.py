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

    def getinventoryID(self) -> int:
        return self.inventoryID

    def setInventoryID(self, user_input: int):
        self.inventoryID = user_input

    def getSKU_ID(self) -> int:
        return self.skuID

    def setSKU_ID(self, user_input: int):
        self.skuID = user_input

    def getUsername(self) -> str:
        return self.username
    
    def getLocation(self) -> str:
        return self.location

    def setLocation(self, user_input: str):
        self.location = user_input

    def getQuantity(self) -> int:
        return self.quantity

    def setQuantity(self, user_input: int):
        self.quantity = user_input
    
    def getStatus(self) -> str:
        return self.status
    
    def setStatus(self, user_input: str):
        self.status = user_input





            
