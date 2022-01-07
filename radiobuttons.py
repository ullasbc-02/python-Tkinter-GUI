from tkinter import *
root = Tk()
root.title('Radio buttons')
CARS = [
    ("Ford", "FORD"),
    ("Fiat", "FIAT"),
    ("Ferrari", "FERRARI"),
]
motor = StringVar()
motor.set("Ford")
for text, cars in CARS :
    Radiobutton(root, text=text, variable=cars, value=motor).pack()
    def clicked(value):
        myLabel= Label(root, text=value)
        myLabel.pack()
myButton = Button(root, text="click me!!", command=lambda:clicked(CARS.get()))
myButton.pack()
root.mainloop()


