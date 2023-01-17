from tkinter import *
import random 

fen = Tk()
fen.geometry('340x100')
fen.configure(padx=5, pady=5, bg="#f1f1f1")
fen.resizable(False, False)


N = StringVar()
double_N = StringVar()

def onEnter(event):
  value_N = N.get()
  if len(double_N.get()) > 0 or len(value_N) == 0:
    entry_show_n.delete(0, END)
  if (value_N == ''): # this condition to ignore the Error |==> ValueError: invalid literal for int() with base 10: '' <==|
    return
  total = int(value_N) * 2
  double_N.set(str(total))

lbl_n = Label(fen, text="Enter The value of N:")
lbl_n.grid(row=0, column=0, padx=30, pady=10)
entry_input_n = Entry(fen, textvariable=N,)
entry_input_n.bind("<Return>", onEnter)
entry_input_n.grid(row=0, column=1)
lbl_double_n = Label(fen, text="Here is the double 2*N:")
lbl_double_n.grid(row=1, column=0)
entry_show_n = Entry(fen, textvariable=double_N)
entry_show_n.grid(row=1, column=1)




fen.mainloop()