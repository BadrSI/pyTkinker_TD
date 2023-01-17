from tkinter import *

fen = Tk()
btn1 = Button(fen, text="Button 1", width=30, padx=10, pady=10).grid(row=0, column=0)
btn2 = Button(fen, text="Button 2", width=30, padx=10, pady=10).grid(row=0, column=1)
btn3 = Button(fen, text="Button 3", width=30, padx=10, pady=10).grid(row=1, column=0)
btn4 = Button(fen, text="Button 4", width=30, padx=10, pady=10).grid(row=1, column=1)
fen.mainloop() 