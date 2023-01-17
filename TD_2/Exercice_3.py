from tkinter import *
import random 

fen = Tk()
fen.configure(padx=5, pady=5, bg="#f1f1f1")
s_value = StringVar()
def resize_window(direction):
  width = fen.winfo_width() 
  height = fen.winfo_height()  
  if direction == 'down' and int(s_value.get()) > 0:
    fen.geometry(str(width - 25)+'x'+str(height - 25))
  elif direction == 'up' and int(s_value.get()) < 25:
    fen.geometry(str(width + 25)+'x'+str(height + 25))

tcl_up_or_down = fen.register(resize_window)

lbl = Label(fen, text="Resize Window:",font=("Segoe ui", 16))
lbl.pack()
s_box = Spinbox(fen, from_=0, to=100,textvariable=s_value, font=("Segoe ui", 16), command=(tcl_up_or_down, '%d'))
# s_box.bind("<Button-1>", increase)
s_box.pack()


fen.mainloop()