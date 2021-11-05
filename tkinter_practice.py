from tkinter import *

root = Tk() # This line must come before anything else; ALWAYS the first step. 

# In Tkinter you must (1) define and create something (2) put it up on the screen.
e = Entry(root) # This can be used to create a simple input field
e.pack()    # See above comment
# Initial Button test below:

def myClick():
    myLabel = Label(root, text=e.get()) # Allows user to write in the input field, returns what they wrote
    myLabel.pack()

myButton = Button(root, text = "Say Something Cool", command=myClick)
myButton.pack()

root.mainloop()
