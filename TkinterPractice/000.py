
from tkinter import *
master = Tk() 
master.title("non")
master.geometry("200x200")
w = Canvas(master, width=40, height=60) 
w.pack() 
canvas_height=20
canvas_width=2000
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
mainloop() 