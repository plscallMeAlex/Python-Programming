from tkinter import *
class me:
    def __init__(self):
        self.window = Tk()
        self.window.title("Spinner")
        self.count = 0        
        self. lb1 = Label(self.window, text=self.count)
        self.lb1.grid(row=2, column=1, columnspan=2)

        but1 = Button(self.window, text="+",command= self.add)
        but2 = Button(self.window, text="-",command=self.sub)
        but3 = Button(self.window, text="Reset", command=self.reset)
        
        but1.grid(column=3, row=1 ,columnspan=2)
        but2.grid(column=3, row=2, columnspan=2)
        but3.grid(column=3, row=3, columnspan=2)

        self.window.mainloop()
    def add(self):
        self.count += 1
        self.update()
    def sub(self):
        self.count -= 1
        self.update()
    def reset(self):
        self.count = 0
        self.update()
    def update(self):
        self.lb1.config(text=self.count)

me()
