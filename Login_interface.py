#This class will display a CLI for the user to log in as a manager, staff, or customer
from verify_login import verifyLogin

verify = verifyLogin()

# The LoginInterface class provides a command-line interface for users to log in as a manager, staff, or customer.
class LoginInterface:
    def __init__(self):
        pass

    def display_login_options(self):
        print("Welcome to the Furniture Management System!")
        print("1. Manager Login")
        print("2. Staff Login")
        print("3. Customer Login")

# The user_choice method prompts the user to select a login option and handles the login process based on the user's choice.
    def user_choice(self):
        while True:
            choice = int(input("Please select an option (1-3): "))

            if choice == 1:
                is_valid = verify.check_manager_credentials(input("Enter Manager Username: "), input("Enter Manager Password: "))
            elif choice == 2:
                is_valid = verify.check_staff_credentials(input("Enter Staff Username: "), input("Enter Staff Password: "))
            elif choice == 3:
                is_valid = verify.check_customer_credentials(input("Enter Customer Username: "), input("Enter Customer Password: "))
            else:
                print("Invalid choice. Please try again.")
                continue

            if is_valid:
                print("Login successful!")
            else:
                print("Invalid username or password.")
            break

