x = open("example.txt", mode="r")
all = ""
for line in x:
	all += line
x.close()  # Be sure to close the file 
print(all)



string = ("\nIt was the season of light,\n" # Remember we need \n to start a new line
		+ "it was the season of darkness.")
x = open("example.txt", mode="a") # Switch to a to append
x.write(string)
x.close() 
# Now let's check the file by reading it
x = open("example.txt", mode="r") # Switch to r to read back in
all = ""
for line in x:
	all += line
x.close() 
print(all)



string = ("\nIt was the season of light,\n" # Remember we need \n to start a new line
		+ "it was the season of darkness.")
x = open("example.txt", mode="a") # Switch to a to append
x.write(string)
string = ("\nIt was the spring of hope,\n"  # Change and add another string
		+ "it was the winter of despair.")
x.write(string)
x.close() 
# Now let's check the file by reading it
x = open("example.txt", mode="r") # Switch to r to read back in
all = ""
for line in x:
	all += line
x.close() 
print(all)