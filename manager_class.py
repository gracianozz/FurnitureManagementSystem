# Artifact Name: manager_class.py
# Description: Implements Manager logic including role-based inventory search.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

import csv

class Manager:
    _id_counter = 0
    
    def __init__(self, fname="", lname="", manager_id=None):
        Manager._id_counter += 1
        self.managerID = manager_id if manager_id is not None else Manager._id_counter
        self.fname = fname
        self.lname = lname

    def getmanagerID(self) -> int:
        return self.managerID
    
    def setFName(self, user_input: str):
        self.fname = user_input

    def getFName(self) -> str:
        return self.fname

    def setLName(self, user_input: str):
        self.lname = user_input

    def getLName(self) -> str:
        return self.lname

    def setUsername(self, user_input: str):
        self.username = user_input

    def getUsername(self) -> str:
        return self.username