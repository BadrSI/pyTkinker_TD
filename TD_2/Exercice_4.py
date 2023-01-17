from tkinter import *
# from tkinter.ttk import *

fen = Tk()
fen.title('Frame')
fen.geometry('200x200')

def enter(event):
    print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))
    frame1.configure(bg='yellow')

def exit_(event):
    print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))
    frame1.configure(bg='black')

frame1 = Frame(fen, height = 200, width = 200, bg='#111')
frame1.bind('<Enter>', enter)
frame1.bind('<Leave>', exit_)
frame1.pack()

fen.mainloop()