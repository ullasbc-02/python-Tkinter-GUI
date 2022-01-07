from tkinter import *
root = Tk()
def myclick():
    myLabel = Label(root, text="Here we go!!", bg="red")
    myLabel.pack()
myButton = Button(root, text="Click me!!", padx=20, pady=20, command=myclick, fg="white", bg="gray")
myButton.pack()
root.mainloop()
