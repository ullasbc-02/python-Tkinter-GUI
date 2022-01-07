from tkinter import *
root = Tk()
root.title('Radio buttons')
r = IntVar()
r.set("1") #setting option value
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()
Radiobutton(root, text="Option_1", variable=r, value=1, command= lambda: clicked()).pack()
Radiobutton(root, text="Option_2", variable=r, value=2, command= lambda: clicked()).pack()
root.mainloop()