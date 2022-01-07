from tkinter import *
from tkinter import messagebox
#showinfo,#showwarning,#showerror,#askquestion,#askokcancel,#askyesno
root = Tk()
root.title('Message box')
def popup():
    response = messagebox.askokcancel("This is popup", "Hello world!!")
    if response == 1:
        Label(root,text="You got it").pack()
    else:
        Label(root,text="you got nothing").pack()


button=Button(root, text="CLICK", command=popup).pack()
root.mainloop()