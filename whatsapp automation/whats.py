import pywhatkit as kit
from datetime import datetime
import tkinter as tk

now = datetime.now()

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 500,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='invia messaggi')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='inserisci il numero di telefono con il +39:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)

label3 = tk.Label(root, text='inserisci il messaggio:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 180, window=label3)

entry2 = tk.Entry (root)
canvas1.create_window(200, 200, window=entry2)


def getSquareRoot():
    x1 = entry1.get()   # numero di telefono
    x2 = entry2.get()   # messaggio
    now = datetime.now()

    h = now.hour
    minutes = now.minute + 1
    if minutes > 60:
        minutes = 00
        h = now.hour + 1
    kit.sendwhatmsg(x1, x2, h, minutes)
    print("numero", x1)
    print("messaggio", x2)
    print("ora", h)
    print("minutes", minutes)
    #kit.send
    pg.press("enter")
    time.sleep(1)

    label4 = tk.Label(root, text=str(x1) , font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)



button1 = tk.Button(text='invia messaggio', command=getSquareRoot, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 300, window=button1)

root.mainloop()

