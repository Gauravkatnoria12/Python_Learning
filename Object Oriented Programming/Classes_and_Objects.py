
class Students:   # Class : blue-print of the object
  name = "Guest"
  roll = 00
  gpa = 00.00

  def __init__(self, name , roll , gpa):
    self.name = name
    self.roll = roll
    self.gpa = gpa


  def show(self):
    print(f"\nName : {self.name} \nRoll No. : {self.roll} \nGPA : {self.gpa}")

s1 = Students("Gaurav", 2525029, 9.8) # Object : instance of class
s1.show()

s2 = Students("Harry", 2525030, 9.0)  # object 
s2.show()

s3 = Students("Patrick", 2525031, 8.8) # object
s3.show()

'''
Output:

Name : Gaurav 
Roll No. : 2525029 
GPA : 9.8

Name : Harry 
Roll No. : 2525030 
GPA : 9.0

Name : Patrick 
Roll No. : 2525031 
GPA : 8.8

'''