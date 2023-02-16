f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

"""
r	Opens a file for reading. (default)
w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Opens a file for exclusive creation. If the file already exists, the operation fails.
a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Opens in text mode. (default)
b	Opens in binary mode.
+	Opens a file for updating (reading and writing)
"""




#closing the file

f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()

#safer to use try catch

try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()


#opening file
with open("lesson1.txt",'w',encoding = 'utf-8') as f:
   f.write("This is my new file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

f.read()

f.seek()
f.tell()
f.readline()