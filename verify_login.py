# Artifact Name: verify_login.py
# Description: Provides backend logic for validating credentials against CSV databases.
# Authors: Gustavo, Mohanad, Ashfaqh, JaQuan, Nate
# Date: April 25, 2026

# The verifyLogin class provides methods to check the credentials of managers, staff, and customers by reading from their respective CSV files.
import csv

class verifyLogin:
    def __init__(self, file_path=None):
        self.file_path = file_path
    
#If option 1 is selected, the manager file of credentials will be checked
    def check_manager_credentials(self, username, password):
        with open("Managers/managers.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row.get("username") == username and row.get("password") == password:
                    return row

        return None
    
#If option 2 is selected, the staff file of credentials will be checked
    def check_staff_credentials(self, username, password):
        with open("Staff/staff.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row.get("username") == username and row.get("password") == password:
                    return row

        return None

#If option 3 is selected, the customer file of credentials will be checked. 
    def check_customer_credentials(self, username, password):
        with open("Customers/customers.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row.get("username") == username and row.get("password") == password:
                    return row

        return None
    

#Sign up method classes to ensure username are unique and not taken

    def _ensure_newline(self, filepath):
        with open(filepath, "rb") as file:
            file.seek(0, 2)
            if file.tell() == 0:
                return
            file.seek(-1, 2)
            if file.read(1) not in (b'\n', b'\r'):
                with open(filepath, "a") as f:
                    f.write('\n')

    def sign_up_manager(self, fname, lname, username, password):
        last_id = 0
        with open("Managers/managers.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("username") == username:
                    print("Username already taken. Please choose a different username.")
                    return False
                last_id = int(row.get("managerID", 0))

        new_id = last_id + 1
        self._ensure_newline("Managers/managers.csv")
        with open("Managers/managers.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_id, fname, lname, username, password])

        print("Manager account created successfully!")
        return True

    def sign_up_staff(self, fname, lname, username, password):
        last_id = 0
        with open("Staff/staff.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("username") == username:
                    print("Username already taken. Please choose a different one.")
                    return False
                last_id = int(row.get("staffID", 0))

        new_id = last_id + 1
        self._ensure_newline("Staff/staff.csv")
        with open("Staff/staff.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_id, fname, lname, username, password])

        print("Staff account created successfully!")
        return True

    def sign_up_customer(self, fname, lname, username, password, address, phoneNum):
        last_id = 0
        with open("Customers/customers.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("username") == username:
                    print("Username already taken. Please choose a different one.")
                    return False
                last_id = int(row.get("customerID", 0))

        new_id = last_id + 1
        self._ensure_newline("Customers/customers.csv")
        with open("Customers/customers.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_id, fname, lname, username, password, address, phoneNum])

        print("Customer account created successfully!")
        return True
    


