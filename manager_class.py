class Manager:
  _id_counter = 0
  
  def __init__(self, fname = "", lname = ""):
    Manager._id_counter+= 1
    self.managerID = Manager._id_counter
    self.fname = fname
    self.lname = lname
    
