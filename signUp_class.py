# Artifact Name: signUp_class.py
# Description: Manages the registration process for new Managers, Staff, and Customers.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

import csv

from verify_login import verifyLogin

verify = verifyLogin()


class signUp:
    def __init__(self):
        pass

    def signUp_choices(self):

        print("Furniture Management System Sign Up Section")

        while True:
            print("1. Manager Sign Up")
            print("2. Staff Sign Up")
            print("3. Customer Sign Up")
            print("4. Back to Main Menu")
            choice = int(input("Choose an option (1-4): "))

            if choice == 1:
                verify.sign_up_manager(input("Enter New Manager First Name: "), input("Enter New Manager Last Name: "), input("Enter New Manager Username: "), input("Enter New Manager Password: "))
                break
            elif choice == 2:
                verify.sign_up_staff(input("Enter New Staff First Name: "), input("Enter New Staff Last Name: "), input("Enter New Staff Username: "), input("Enter New Staff Password: "))
                break
            elif choice == 3:
                verify.sign_up_customer(input("Enter New Customer First Name: "), input("Enter New Customer Last Name: "), input("Enter New Customer Username: "), input("Enter New Customer Password: "), input("Enter New Customer Address: "), input("Enter New Customer Phone Number: "))
                break
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
