#The start of the Furniture Recommendation System

from Login_interface import LoginInterface

# Create an instance of the LoginInterface
login = LoginInterface()

# Display the login options to the user
login.display_login_options()

# Prompt the user to select a login option and handle the login process
login.user_choice()
