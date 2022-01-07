from tkinter import *
root = Tk()
myEntry = Entry(root)
myEntry.pack()
myEntry.insert(0, "Enter name here")
def myclick():
    myLabel = Label(root, text="Hello " + myEntry.get(), bg="white")
    myLabel.pack()
myButton = Button(root, text="Enter your Name", padx=20, pady=20, command=myclick, fg="white", bg="gray")
myButton.pack()
root.mainloop()
