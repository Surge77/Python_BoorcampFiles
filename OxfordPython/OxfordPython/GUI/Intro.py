from tkinter import *

root = Tk()  # creates a window

# we will write our main code in between root and mainloop method

root.geometry('720x480')   # width x height

# fg means foreground and bg means background of title
title = Label(root, text="First window",fg="#FACBCB",font=('',50),) # the second element in tuple is responsible for font size
title.pack()
btn1 = Button(root,text='Click me!')
btn1.pack(side=TOP)  # A dynamic layout to show the widgets i.e it adjust the button position as we resize it


root.mainloop()  # loops the window until we close