#sets  are used to store multiple items in a single variable.


my_fruits = {"apple", "banana", "cherry","guave","orange"}

print(my_fruits)

for fruit in my_fruits:
  print(fruit)

print(type(my_fruits))
print(len(my_fruits))

#functions 
#A function is a block of code which only runs when it is called.

def my_function():
  print("Hello from a function")

my_function()

#argumants 
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


#Python Dates
import datetime

x = datetime.datetime.now()
print(x)

#Date Object
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#try except 

#Friday
# Object Oriented Programming 


# Class and Objects 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#Inheritance 



#File Handling 
# Open ,close file