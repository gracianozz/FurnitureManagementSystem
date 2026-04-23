import csv
# The verifyLogin class provides methods to check the credentials of managers, staff, and customers by reading from their respective CSV files.
class verifyLogin:
    def __init__(self, file_path=None):
        self.file_path = file_path
    
#If option 1 is selected, the manager file of credentials will be checked
    def check_manager_credentials(self, username, password):
        with open("Managers/managers.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row.get("username") == username and row.get("password") == password:
                    return True

        return False
    
#If option 2 is selected, the staff file of credentials will be checked
    def check_staff_credentials(self, username, password):
        with open("Staff/staff.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row.get("username") == username and row.get("password") == password:
                    return True
                
        return False

#If option 3 is selected, the customer file of credentials will be checked. 
    def check_customer_credentials(self, username, password):
        with open("Customers/customers.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row.get("username") == username and row.get("password") == password:
                    return True

        return False
    
