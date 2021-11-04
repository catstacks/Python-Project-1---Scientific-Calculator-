from tkinter import *

root = Tk() # This line must come before anything else; ALWAYS the first step. 

# In Tkinter you must (1) define and create something (2) put it up on the screen.    
# Initial Button test below:

def myClick():
    myLabel = Label(root, text="The button click worked!!")
    myLabel.pack()

myButton = Button(root, text = "Click here!", command=myClick)
myButton.pack()

root.mainloop()
