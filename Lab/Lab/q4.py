from tkinter import *
from tkinter import messagebox
import random


class Frec:
    def __init__(self):
        self.window = Tk()
        self.cv =Canvas(self.window, bg="white", width=600, height=400)
        self.cv.pack(fill=BOTH, expand=True)
        self.displayrec()
        self.cv.bind("<Button-1>",self.draw)
        self.window.mainloop()
    def draw(self, event):
        a = ["white", "blue", "black", "green", "red", "yellow", "pink"]
        x1 = event.x; x2 = event.x; y1 = event.y; y2 = event.y
        if 50 <= event.x <= 400 and 50 <= event.y <= 250:
            self.cv.create_oval(x1, y1, x2+10, y2+10, fill = random.choice(a))
        else:
            messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle")
    def displayrec(self):
        self.cv.create_rectangle(50, 50, 400, 250, outline="black", tags = "rec")
    
Frec()


