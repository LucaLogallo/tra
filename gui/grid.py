from tkinter import *

root = Tk()

myLabel1 = Label(root, text="ciao")  # .grid(row=0, column=0)
myLabel2 = Label(root, text="mi chiamo luca")  # .grid(row=1, column=1)
#myLabel3 = Label(root, text="")
#myLabel4 = Label(root, text="")

# posso fare sia così che mettere direttamente in coda quando li creo
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
#myLabel3.grid(row=0, column=1)
#myLabel4.grid(row=0, column=2)


root.mainloop()
