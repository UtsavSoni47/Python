class Student:
 #this is constructor
  def __init__(self,n=".",m=0):
    self.name=n
    self.marks=m
 #this is an instance method
  def display(self):
   print("Hi",self.name)
   print("Your marks",self.marks)
#constuctor is called without any arguments
s=Student()
s.display()
print("--------------")
#constructor is called with 2 arguments
s1=Student("xyz",85)
s1.display()
print("-------------")
