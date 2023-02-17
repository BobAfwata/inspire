#!/usr/bin/env python3

# This is a single line comment 
# strings operations in python 
# Name : Bob Afwata
# Email : bob@focuslense.co.ke
# Date : 17th Feb 2023
# File : strings.py

poem = """ This is a poem about nothing
           Its funny people laugh about nothing        
"""

print(poem)

print(len(poem))

f_name = "Bob"
s_name = "Afwata"

full_name = f_name + s_name

age = 25  # years 
print("My name is " +full_name+"and I am " +str(age)+ "years old ")

print("My name is {} and I am {} years old ".format(full_name,age))


print("Hello from Mary \n How are you \n I am fine")
print("Hello from Mary \t How are you \t I am fine")