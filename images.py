from tkinter import *

from PIL import ImageTk
from PIL import Image

root = Tk()
#Creating a icon
root.iconbitmap('share-icon.png')
root.title('Learn to code')
#opening an image
my_image = ImageTk.PhotoImage(Image.open("share-icon.png"))
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()
my_label = Label(image=my_image)
my_label.pack()
root.mainloop()
