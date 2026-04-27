from inventory_control import inventory_control

class FurnitureMenu:
    def __init__(self):
        # Create an instance of the control class to use its methods
        self.control = inventory_control()

    def Inventory_menu(self):
        while True:
            print("\n--- Furniture Inventory System ---")
            print("1. Add Furniture")
            print("2. Remove Furniture")
            print("3. Edit Furniture")
            print("4. Exit")
            
            try:
                choice = int(input("\nSelect an option (1-4): "))
            except ValueError:
                print("Invalid input. Please enter a number from 1-4.")
                continue

            if choice == 1:
                name = input("Enter the name of the furniture: ")
                self.control.add_furniture(name)
            
            elif choice == 2:
                term = input("Enter name of the furniture to remove: ")
                self.control.remove_furniture(term)
            
            elif choice == 3:
                term = input("Enter name of the furniture to edit: ")
                self.control.edit_furniture(term)
            
            elif choice == 4:
                print("Exiting system. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")

# To run the program:
if __name__ == "__main__":
    app = FurnitureMenu()
    app.Inventory_menu()
