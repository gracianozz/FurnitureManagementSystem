from furniture_Search import Furniture_Search
from place_order import Place_Order
from order_class import Order
from customer_support import CustomerSupport
from stock_notifier import stock
from inventory_control import manage_inventory

search = Furniture_Search()
place_order = Place_Order()
support = CustomerSupport()
stocks = stock()
inventory = manage_inventory()

class Main_Interfaces:
    def __init__(self):
        pass


#This is where the customer can search for furniture, view orders, etc
    def Customer_Interface(self, customer):
        print(f"Welcome, {customer.getFName()} {customer.getLName()}!\n")
        print("Customer Menu:")
        print("1. Furniture Search")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Customer Support")
        choice = int(input("Please select an option (1-4): "))

        if choice == 1:
            search.FurnitureSearch()

        elif choice == 2:
            place_order.PlaceOrder()

        elif choice == 3:
            Order.viewOrders(customer.getCustomerID())
        
        elif choice == 4:
            support.support_options()




#This is where the staff can view orders, help customers, etc
    def Staff_Interface(self, staff):
        print(f"Welcome, {staff.fname} {staff.lname}!")
        print("Staff Menu")
        print("1. Customer Support")
        print("2. Furniture Search")
        staffChoice = int(input("Please select an option (1-2): "))

        if staffChoice == 1:
            support.contact_support()
        elif staffChoice == 2:
            search.FurnitureSearch()



#This is where the manager can manage inventory, get stock alerts, etc
    def Manager_Interface(self, manager):
        print(f"Welcome, {manager.fname} {manager.lname}!")
        print("Manager Menu")
        print("1. Check Stock Alerts")
        print("2. Manage Inventory")
        print("3. Place Inventory Order")
        managerChoice = int(input("Please select an option (1-3): "))

        if managerChoice == 1:
            stocks.check_stock()
        
        elif managerChoice == 2:
            inventory.manage_inventory()
        
        elif managerChoice == 3:
            inventory.manage_order()