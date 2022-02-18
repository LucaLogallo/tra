from tkinter import *

root = Tk()  # la prima cosa che si apre la finestra iniziale

# widget finestra
myLabel = Label(root, text="Ciao")

myLabel.pack()  # lo inserisco nel package

# quando si ha un programma è continuamente in un loop infinito. Quando clicco su un tasto continua a fare un loop ma cambiano alcune cose

root.mainloop()
