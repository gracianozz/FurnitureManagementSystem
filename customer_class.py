class CustomerClass:
  _id_counter = 0
  
  def __init__(self):
    CustomerClass._id_counter+= 1
    self.customerID = CustomerClass._id_counter
    self.fname = ""
    self.lname = ""
    self.username = ""
    self.address = ""
    self.pnumber = 0

  def getCustomerID(self) -> int:
    return self.customerID
    
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

  def setAddress(self, user_input: str):
    self.adress = user_input

  def getAdress(self) -> str:
    return self.adress

  def setPNumber(self, user_input: int):
    self.pnumber = user_input

  def getPNumber(self) -> int:
    return self.pnumber
