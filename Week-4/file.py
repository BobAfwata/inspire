
#exception handling
filename = 'test.txt'
try:
    for file in filename:
        with open(filename,'r+w',encoding=None) as f_obj:
            contents = f_obj.read()
            print(contents)

    
except FileNotFoundError:
    msg = "Sorry, the file "+ filename + "does not exist."
    print(msg) # 





f = open("C:\\Users\\USER\\Documents\\Inspire-Youth-In-STEM\\Week-4\\test.txt", "r+w+a")
print(f.read())