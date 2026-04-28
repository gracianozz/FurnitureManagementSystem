# Artifact Name: customer_support.py
# Description: Interface logic for customer support options and contact methods.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

import csv
CustomerSupport_PATH = "CustomerSupport/customerSupport.csv"
class CustomerSupport:
    def __init__(self):
        pass

    # Customer view 
    def support_options(self, customerID: int, customerfName: str):
        print("Welcome to Customer Support! How can we assist you today?")
        print("1. Enter a new support enquiry: ")
        print("2. View response(s) to my support enquiries(if any): ")
        

        customerID= str(customerID)
        customerfName = str(customerfName)
        try:
            choice = int(input("Please select an option (1-2): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1-2.")
            return

        if choice == 1:
            message = input("Please enter your support enquiry:")
            with open(CustomerSupport_PATH, "a", newline="") as file:
                fieldnames = ["supportID", "customerID", "customerfName", "CustomerMessage", "staffResponse", "staffID"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Generate supportID
                with open(CustomerSupport_PATH, "r") as file:
                    rows = list(csv.DictReader(file))
                    supportID = max(int(r["supportID"]) for r in rows) + 1 if rows else 1

                # append mode, customer inputs message, fName and IDs are auto-assigned
                writer.writerow({
                    "supportID": supportID,
                    "customerID": customerID,
                    "customerfName": customerfName,
                    "CustomerMessage": message,
                    "staffResponse": "", #
                    "staffID": '0'
                })
        else:
            print("Here are your support enquiries and their responses(if any):")
            with open(CustomerSupport_PATH, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row.get("customerID") == customerID:
                        print(f"Support ID: {row['supportID']} | Message: {row['CustomerMessage']} | Response: {row['staffResponse'] if row['staffResponse'] else 'No response yet.'}")


    # Staff view
    def contact_support(self, staffID: int):
        print("Connecting to customer support...")

        print("Displaying customer support enquiries yet to be responded to:")
        # Find all tickets where staff ID is 0
        with open(CustomerSupport_PATH, "r") as file:
            reader = csv.DictReader(file)

            notResponded = []

            for row in reader:
                if row.get("staffID") == '0':
                    notResponded.append(row)
            
            if not notResponded:
                print("No support enquiries awaiting response.")
                return

            for enquiry in notResponded:
                print(f"Support ID: {enquiry['supportID']} | Customer ID: {enquiry['customerID']} | Customer Name: {enquiry['customerfName']} | Message: {enquiry['CustomerMessage']}")

        # Select ticket
        support_id = input("Enter the support ID you want to respond to (or 'q' to quit): ")

        if support_id.lower() == 'q':
            print("Exiting customer support.")
            return
        else:
            response = input("Enter your response to the customer: ")

            # Update record with response
            updated_rows = []
            with open(CustomerSupport_PATH, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row.get("supportID") == support_id:
                        row["staffID"] = str(staffID)
                        row["staffResponse"] = response
                    updated_rows.append(row)

            # Add response to csv, overwrites existing csv with updated version
            with open(CustomerSupport_PATH, "w", newline="") as file:
                fieldnames = ["supportID", "customerID", "customerfName", "CustomerMessage", "staffResponse", "staffID"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated_rows)

            print("Response sent to customer and support enquiry updated.")




        
