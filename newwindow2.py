from tkinter import *
from PIL import ImageTk
from PIL import Image
root = Tk()
root.title('Window')
def open():
    global my_image
    top = Toplevel()
    top.title('My second window')
    Label(top, text="New window again!!").pack()
    my_image = ImageTk.PhotoImage(Image.open("share-icon.png"))
    my_Label = Label(top, image=my_image).pack()
    button = Button(top, text="Close", command=top.destroy).pack()

button1=Button(root, text="Open", command=open).pack()


root.mainloop()