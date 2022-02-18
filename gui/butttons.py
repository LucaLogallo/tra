from tkinter import *

root = Tk()

# creo una funzione


def myClick():
    myLabel = Label(root, text="aia", fg="green")
    myLabel.pack()


# si può aggiungere uno state state=DISABLED
# padx la larghezza
# pady l'altezza
# fg per il colore del testo
# bg per il colore sfondo
myButton = Button(root, text="click here", padx=50, pady=10,
                  command=myClick, fg="blue", bg="red")

myButton.pack()

root.mainloop()
