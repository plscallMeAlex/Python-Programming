import math
from tkinter import *

class DrawTree:
    def __init__(self):
        self.count = 0
        window = Tk()
        window.title("Recursive Tree")
        self.drawscreen = Canvas(window, width=500, height=500)
        self.drawscreen.pack()

        frame0 = Frame(window)
        frame0.pack()

        txt = Label(frame0, text="Enter the Depth")
        txt.grid(row=0, column=0, sticky="w", padx=10)

        self.enter = Entry(frame0)
        self.enter.grid(row=0, column=1, columnspan=2)

        txt1 = Label(frame0, text="Display")
        txt1.grid(row=0, column=3, sticky="e", padx=10)

        bu1 = Button(frame0, text="Save", command=lambda: self.value())
        bu1.grid(row=0, column=4, padx=20)

        window.mainloop()

    def value(self):
        self.drawscreen.delete(ALL)
        self.count = int(self.enter.get())
        self.drawing(250, 400, self.count, 90, 100)

    def drawing(self, x, y, depth, angle, length):
        if depth >= 0:
            x_end = x + int(length * math.cos(math.radians(angle)))
            y_end = y - int(length * math.sin(math.radians(angle)))

            self.drawscreen.create_line(x, y, x_end, y_end, width=2, fill="green")
            self.drawing(x_end, y_end, depth - 1, angle - 30, length * 0.7)
            self.drawing(x_end, y_end, depth - 1, angle + 30, length * 0.7)

DrawTree()
