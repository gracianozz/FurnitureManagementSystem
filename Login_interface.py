# Artifact Name: Login_interface.py
# Description: Boundary class providing the main CLI for user authentication and role-based routing.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

#This class will display a CLI for the user to log in as a manager, staff, or customer
from verify_login import verifyLogin
from signUp_class import signUp
from main_interfaces import Main_Interfaces
from manager_class import Manager
from staff_class import Staff
from customer_class import Customer



#Create instances of the verifyLogin, signUpm and main interfaces
verify = verifyLogin()
sign_up = signUp()
main_interfaces = Main_Interfaces()

# The LoginInterface class provides a command-line interface for users to log in as a manager, staff, or customer.
class LoginInterface:
    def __init__(self):
        pass


# The user_choice method prompts the user to select a login option and handles the login process based on the user's choice.
    def display_login_menu(self):
        print("Welcome to the Furniture Management System!")
        print("Here are the available options to Log in / Sign up: ")

        while True:
            print("1. Manager Login")
            print("2. Staff Login")
            print("3. Customer Login")
            print("4. Sign Up")
            print("5. Exit")

            try:
                choice = int(input("Please select an option (1-5): "))
            except ValueError:
                print("Invalid input. Please enter a number corresponding to the options.")
                print("===============================================")
                continue

            if choice == 1:
                row = verify.check_manager_credentials(
                    input("Enter Manager Username: "),
                    input("Enter Manager Password: ")
                )
                if row:
                    manager = Manager(fname=row["fName"], lname=row["lName"], manager_id=int(row["managerID"]))
                    main_interfaces.Manager_Interface(manager)
                    break
                else:
                    print("Invalid credentials. Please try again.")

            elif choice == 2:
                row = verify.check_staff_credentials(
                    input("Enter Staff Username: "),
                    input("Enter Staff Password: ")
                )
                if row:
                    staff = Staff(fname=row["fName"], lname=row["lName"], staff_id=int(row["staffID"]))
                    main_interfaces.Staff_Interface(staff)
                    break
                else:
                    print("Invalid credentials. Please try again.")

            elif choice == 3:
                row = verify.check_customer_credentials(
                    input("Enter Customer Username: "),
                    input("Enter Customer Password: ")
                )
                if row:
                    customer = Customer(customer_id=int(row["customerID"]))
                    customer.setFName(row["fName"])
                    customer.setLName(row["lName"])
                    customer.setUsername(row["username"])
                    customer.setAddress(row["address"])
                    customer.setPNumber(int(row["PNumber"]))
                    main_interfaces.Customer_Interface(customer)
                    break
                else:
                    print("Invalid credentials. Please try again.")

            elif choice == 4:
                sign_up.signUp_choices()

            elif choice == 5:
                print("Exiting the Furniture Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
        

