class Staff:
  _id_counter = 0
  
  def __init__(self, fname = "", lname = "", job_title =""):
    Staff._id_counter+= 1
    self.staffID = Staff._id_counter
    self.fname = fname
    self.lname = lname
    self.job_title = job_title
    
