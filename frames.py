from tkinter import *
root = Tk()
frame = LabelFrame(root, text="This is my frame", padx=10, pady=10)
frame.pack(padx=10, pady=10)
button = Button(frame, text="dont click")
button.pack()
root.mainloop()
