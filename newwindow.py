from tkinter import *
from PIL import ImageTk
from PIL import Image
root = Tk()
root.title('Window')
top = Toplevel()
Label(top, text="New window again!!").pack()
my_image = ImageTk.PhotoImage(Image.open("share-icon.png"))
my_Label=Label(top, image=my_image).pack()
root.mainloop()