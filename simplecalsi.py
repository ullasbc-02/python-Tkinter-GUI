from tkinter import *
root = Tk()
root.title('Simple calculator')
myEntry = Entry(root, width=30, borderwidth=10)
myEntry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_click(number):
   current = myEntry.get()
   myEntry.delete(0, END)
   myEntry.insert(0, str(current) + str(number))
def button_clear():
    myEntry.delete(0, END)
def button_add():
    first_number = myEntry.get()
    global f_num
    f_num = int(first_number)
    myEntry.delete(0, END)
def button_equal():
    second_number = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, f_num + int(second_number))


myButton1 = Button(root, text="1", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(1))
myButton2 = Button(root, text="2", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(2))
myButton3 = Button(root, text="3", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(3))
myButton4 = Button(root, text="4", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(4))
myButton5 = Button(root, text="5", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(5))
myButton6 = Button(root, text="6", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(6))
myButton7 = Button(root, text="7", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(7))
myButton8 = Button(root, text="8", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(8))
myButton9 = Button(root, text="9", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(9))
myButton0 = Button(root, text="0", padx=20, pady=20, fg="white", bg="gray", command= lambda: button_click(0))
myButtonequals = Button(root, text="=", padx=55, pady=20, fg="white", bg="black", command= button_equal)
myButtonadd = Button(root, text="+", padx=20, pady=20, fg="white", bg="gray", command= button_add)
myButtonclear = Button(root, text="Clear", padx=45, pady=20, fg="white", bg="gray", command= button_clear)

myButtonequals.grid(row=5, column=1, columnspan=2)
myButtonadd.grid(row=5, column=0)
myButtonclear.grid(row=4, column=1, columnspan=2)

myButton1.grid(row=1, column=0)
myButton2.grid(row=1, column=1)
myButton3.grid(row=1, column=2)

myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)

myButton7.grid(row=3, column=0)
myButton8.grid(row=3, column=1)
myButton9.grid(row=3, column=2)
myButton0.grid(row=4, column=0)




# button_quit = Button(root, text="Exit program", command=root.quit)
# button_quit.grid(row=7, column=2)
root.mainloop()