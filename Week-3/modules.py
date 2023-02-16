import platform

x = platform.system()
print(x)

import time
seconds = time.time()
print("Seconds since epoch =", seconds)


import time

result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)


# Python program to display calendar of
# given month of the year
 
# import module
import calendar
 
yy = 2022
mm = 6
 
# display the calendar
print(calendar.month(yy, mm))


# Python program to display calendar of
# given year
 
# import module
import calendar
 
yy = 2017
 
# display the calendar
print(calendar.calendar(yy))