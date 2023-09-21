from tkinter import *

class Drw:
    def __init__(self):
        self.window = Tk()
        self.window.title("A simple paint program")
        self.cv = Canvas(self.window, bg="white", width=200, height=100)
        self.cv.pack()

        self.cv.bind("<B1-Motion>", self.paint)

        lb1 = Label(self.window, text="Drag the mouse to draw")
        lb1.pack()

        but1 = Button(self.window, text="Clear", command=self.clear)
        but1.pack()

    def clear(self):
        self.cv.delete(ALL)

    def paint(self, event):
        x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x + 3), (event.y + 3)
        self.cv.create_line(x1, y1, x2, y2, fill="#000000")

drw = Drw()

drw.window.mainloop()
