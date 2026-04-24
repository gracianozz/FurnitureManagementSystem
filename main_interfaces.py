class Main_Interfaces:
    def __init__(self):
        pass

#This is where the customer can search for furniture, view orders, etc
    def Customer_Interface(self, customer):
        print(f"Welcome, {customer.getFName()} {customer.getLName()}!")
        print("Customer Menu")


#This is where the staff can view orders, help customers, etc
    def Staff_Interface(self, staff):
        print(f"Welcome, {staff.fname} {staff.lname}!")
        print("Staff Menu")


#This is where the manager can manage inventory, get stock alerts, etc
    def Manager_Interface(self, manager):
        print(f"Welcome, {manager.fname} {manager.lname}!")
        print("Manager Menu")
