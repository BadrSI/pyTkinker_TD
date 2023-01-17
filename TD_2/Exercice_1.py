from tkinter import *
import random 

fen = Tk()
fen.title('Cercles')
fen.geometry('370x410')
fen.configure(padx=5, pady=5, bg="#f1f1f1")

def change_outline_color():
  global COLOR
  COLOR = 'blue'
  colors = ['purple', 'cyan', 'green', 'red', 'blue', 'orange', 'black']
  COLOR = colors[random.randint(0, len(colors)-1)]
  print(COLOR)

def gernarate_circle():
  x1 = random.randint(50, 250)
  y1 = random.randint(50, 250)
  radius = random.randint(10, 40) 
  print(x1, y1, radius, COLOR)
  canvas.create_oval( x1, y1, (x1 + (radius *2)), (y1 + (radius *2)), width=2, outline=COLOR)
  
def clear():
  canvas.delete('all')



canvas = Canvas(fen, width=360, height=360, bg='white')
canvas.pack()


COLOR = 'blue'

btn_tracer_cercle = Button(fen, text='Tracer un cercle', padx=5, command=gernarate_circle)
btn_tracer_cercle.pack(side='left', expand=True)
btn_chonger_couleur = Button(fen, text='Nouvelle de couleur', padx=5, command=change_outline_color)
btn_chonger_couleur.pack(side='left', expand=True)
btn_effacer = Button(fen, text='Effacer', padx=5, command=clear)
btn_effacer.pack(side='left', expand=True)
btn_quitter = Button(fen, text='Quitter', padx=5, command=fen.destroy)
btn_quitter.pack(side='left', expand=True)

fen.mainloop()