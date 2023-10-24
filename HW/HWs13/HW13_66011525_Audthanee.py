#===========================================================================================================================
#Q1
def print_btree(l, d):
    for i in l:
        put = ". " * d + str(i)
        if type(i) != list:
            print(put)
        else:
            print_btree(i,d+1)


print_btree([1,[[11,[111,112]],[12,[121,[122,[1221,1222]]]]]],0)

#===========================================================================================================================
#Q2
def f(n):
    if n == 0:
        print(0)
        return 0
    if n > 0 and n % 2 == 0:
        a = 2 * f(n/2) + 1
        print(n)
        print(a)
        return a
    else:
        print(0)
        return 0
    print(n)

f(4)

#===========================================================================================================================
#Q3_1
def perm2(t):
    newt = list(t)
    if len(t) == 1:
        return [newt]
    else:
        r = []
        for i in range(len(newt)):
            su = newt[0:i] + newt[i+1:]
            tuplex = perm2(su)
            for j in tuplex:
                r.append(newt[i:i+1] + j)
        return r

def permprint(t):
    a = perm2(t)
    for i in a:
        print(tuple(i[0:2]))

permprint((1, 2, 3))

#===========================================================================================================================
#Q3_2
def perm3(t):
    newt = list(t)
    if len(t) == 1:
        return [newt]
    else:
        r = []
        for i in range(len(newt)):
            su = newt[0:i] + newt[i+1:]
            tuplex = perm3(su)
            for j in tuplex:
                r.append(newt[i:i+1] + j)
        return r

def permprint(t):
    a = perm3(t)
    for i in a:
        print(tuple(i[0:3]))

permprint((1, 2, 3))

#===========================================================================================================================
#Q3_3
def perm(t):
    newt = list(t)
    if len(t) == 1:
        return [newt]
    else:
        r = []
        for i in range(len(newt)):
            su = newt[0:i] + newt[i+1:]
            tuplex = perm(su)
            for j in tuplex:
                r.append(newt[i:i+1] + j)
        return r

def permprint(t,n):
    a = perm(t)
    for i in a:
        print(tuple(i[0:n]))

permprint((1, 2, 3), 3)

#===========================================================================================================================
#Q4
def hanoi(n, begin, operate, end):
    if n == 1:
        print(f"Move disk 1 from {begin} to {end}")
        return
    hanoi(n-1, begin, end, operate)
    print(f"Move disk {n} from {begin} to {end}")
    hanoi(n-1, operate, begin, end)

n = 3
begin_peg = "A"
operate_peg = "B"
end_peg = "C"
hanoi(n, begin_peg, operate_peg, end_peg)

#===========================================================================================================================
#Q5
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

#===========================================================================================================================