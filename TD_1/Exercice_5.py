from tkinter import *

fen = Tk()

btn = Button(fen, text="fermer la fenetre !", command=fen.destroy)
btn.pack()

fen.mainloop()