from tkinter import *

root = Tk()




def onClick():
    message = Label(root, text=e.get())
    message.pack()


myButton = Button(root, text="invio", command=onClick)
e = Entry(root, width=100, bg="green", fg="blue")

myButton.pack()
e.pack()
root.mainloop()
