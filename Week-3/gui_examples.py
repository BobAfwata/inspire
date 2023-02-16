#!/usr/bin/python

###########################
#   Name  : Bob Afwata
#   gui_examples using ktinker
#   Date  7/6/2022
##########################

from tkinter import *

window = Tk()
window.title("My Awesome App")
window.configure(bg='white')
window.geometry("400x400") # fix the window size
def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up Window")
    top.configure(bg= 'green')
    msg= Label(top,text= "Welcome to pop up" )


f_name = Label(window, text="First Name", font=("Arial ", 20))
s_name = Label(window, text="Second Name", font=("Arial ", 20))

f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row = 120)

btn = Button(window,text = "Sign Up",bg='blue',fg='red', command= open_popup().pack())
btn.grid(column = 100 , row = 180)

f_name_box = Entry(window ,width=20)
f_name_box.grid(column = 100 , row = 100)

s_name_box = Entry(window ,width=20)
s_name_box.grid(column = 100 , row = 120)




window.mainloop()