# Artifact Name: staff_class.py
# Description: Implements Staff logic with dynamic login, full toolset, and input validation.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

import csv
import os

class Staff:
    def __init__(self, staff_id, fname=None, lname=None):
        self.staffID = staff_id
        self.fname = fname or "Unknown"
        self.lname = lname or ""

    def getstaffID(self) -> int:
        return self.staffID
    
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
        
