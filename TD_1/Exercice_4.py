from tkinter import *

fen = Tk()

def sayhellow():
  lbl = Label(fen, pady=20)
  lbl.grid(row=0)
  lbl.configure(text="Hello World")

btn = Button(fen, text="Button de commande", padx=10, pady=6)
btn.grid(row=1)
btn.configure(command=sayhellow)

fen.mainloop()