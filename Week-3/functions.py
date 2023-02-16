#!/usr/bin/python


#functions 

x = 2
y = 3 
sum = x + y 


#initialize function
def sum_numbers(f_num,s_num):  # f_num and s_num parameters 
    sum_nums = f_num + s_num
    print(sum_nums)

# y = mx + c         linear 
# y = ax^2 + bx + c  Quadratic 

def linear_equation(m,x,c):
    y = (m * x) + c
    return y

def quadratic_equation(a,x,b,c):
    y = a*(x**2) + b*x + c 
    return y 


#call the function
# all blocks of code are run togther
sum_numbers(4,3)
x = 2
print(x) #ok
print("x :" + str(x))

print("x : " + str(x) + "  y :" +str(linear_equation(2,x,7))) 
a = int(input("Enter the co-efficient of first term :"))
b = int(input("Enter the co-efficient of second term :"))
c = int(input("enter constant :"))
#Graph Quadratic equation
===================================================
x   0 ................................+5
y   3  5   7     9                    11 
==================================================