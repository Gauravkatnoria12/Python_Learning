
class Parent:
  def show1(self):
    print("Parent Class")

class Child(Parent):
  def show2(self):
    print("Child Class")

a = Child()
a.show1()
a.show2()

'''
Output:
Parent Class
Child Classs

'''