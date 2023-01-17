from tkinter import *

fen = Tk()

greeting_lbl = Label(fen, text="", name='greeting_lbl')
def validate():
  name = input_entry.get().capitalize().strip()
  print(len(name))
  if (len(name) != 0):
    greeting_lbl.grid(row=2, column=1, pady=10)
    greeting_lbl.configure(text="Bienvenue " + str(name))
  else:
    greeting_lbl.grid_remove()


input_lbl = Label(fen, text="Enter your name").grid(row=0, column=0, padx=10)

input_entry = Entry(fen)
input_entry.grid(row=0, column=1, pady=10)

btn = Button(fen, text="validate", command=validate, padx=40)
btn.grid(row=1, column=1, padx= 20) 




fen.mainloop()