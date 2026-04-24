class Manager:
  _id_counter = 0

  def __init__(self, fname="", lname="", manager_id=None):
    Manager._id_counter += 1
    self.managerID = manager_id if manager_id is not None else Manager._id_counter
    self.fname = fname
    self.lname = lname
    