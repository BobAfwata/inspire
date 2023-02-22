# Advanced Data types 

# Mutable vs immutable 

# Mutable are data types that can change / edited during program lifecycle
# add / remove elements 
# immutable --> Data types that cannot be edited during program lifecycle 

# 1)  List (muatable )

friends = ["Mark","Anita","Faith","Leon"]
#   or   friends = []  for empty list
#  add ---> append() , extend()
# remove --> pop()  del()
studets = ["Marie","Kigen","Serphine"]

friends.extend(studets)
friends.append("James")
friends.sort()
friends.reverse()

# 2) Tuples (immutable)
# Type of list that are immutable

stationaries = ("pens","ink","sharpener","stepler")

# replace the whole tuple 
stationaries = ("ruler","clipboard","eraser")

for stationary in stationaries:
    print(stationary)

numbers = (1,2,4,6,7,8,9,76,89)
print(numbers)
# 3) Dictionaries aka dict 

# uses key and value pair to store data 

student = {"name" : "Bob", "age" :24 , "gender":"Male","is_tall" :True}

print(student["name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])

print(student.values())
print(student.keys())

# "name" : "Bob"  --> name(key) Bob(value)

# 4) Sets 