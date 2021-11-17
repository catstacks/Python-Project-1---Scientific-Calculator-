from tkinter import *

root = Tk() # This line must come before anything else; ALWAYS the first step. 

# In Tkinter you must (1) define and create something (2) put it up on the screen.
e = Entry(root, width=50) # This can be used to create a simple input field and set its width
e.pack()    # See above comment
e.insert(0, "Write something cool: ") # This sets a default value in the input field. Index 0 is used becasue there is only one input field box. 

# Initial Button test below:

def myClick():
    myLabel = Label(root, text=e.get()) # Allows user to write in the input field, returns what they wrote
    myLabel.pack()

myButton = Button(root, text = "Say Something Cool", command=myClick)
myButton.pack()

root.mainloop()
