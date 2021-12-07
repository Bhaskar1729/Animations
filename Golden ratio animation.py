from tkinter import *
import time
import math

tk = Tk()

canvas = Canvas(tk, height = 800, width = 800)
canvas.pack()
r = 0
label = Label(tk)
label.place(x = 50, y = 50)
time.sleep(2)
while r < 1:
    bud = canvas.create_oval(395, 345, 405, 355, fill = "yellow")
    rad = 10
    label.config(text = str(r))
    x = r*2*math.pi - (math.pi)/2

    for i in range(1, 200):
        rad = rad + 0.75
        pos = canvas.coords(bud)
        canvas.move(bud, rad*math.cos(x), rad*math.sin(x))
        pos = canvas.coords(bud)
        bud = canvas.create_oval(pos[0], pos[1], pos[2], pos[3], fill = "yellow")
        x = x + r*2*math.pi             
    tk.update()
    r += 0.0001
    time.sleep(0.001)
    canvas.delete("all")
    
