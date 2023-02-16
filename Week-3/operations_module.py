#!/usr/bin/python
############################
#    Name : Bob Afwata
#    file :operations_module.py
#    Date  : 6/6/2022
##############################

import operations
from student import student

from teachers import Teachers

print(operations.add_numbers(3,5))
print(operations.mult_numbers(300,2))
print(operations.sub_numbers(40,3))
print(operations.div_numbers(4,2)) 

new_student = student("Joan ","cycling",1997)

new_teacher = Teachers("Mr John",12467,"Literature",60000)

print(new_teacher.get_tsc_no())
student.greet_student()