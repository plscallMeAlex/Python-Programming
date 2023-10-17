#Q1-----------------------------------------------------------------------------------------------------------------

from tkinter import *
import time

class Clock(object):
    def __init__(self, hh=0, mm=0, ss=0):
        self.h = hh
        self.m = mm
        self.s = ss
        self.running = True
    
    def run(self, label):
        if self.running:
            self.s += 1
            if self.s == 60:
                self.s = 0
                self.m += 1
            if self.m == 60: 
                self.m = 0
                self.h += 1
            if self.h == 24:
                self.h = 0
            time_str = "{:02d}:{:02d}:{:02d}".format(self.h, self.m, self.s)
            label.config(text=time_str)
        root.after(1000, self.run, label)  # Update the tkinter windo
    def stop(self):
        self.running = False
    
    def setTime(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

class AlarmClock(Clock):
    def __init__(self, hh=0, mm=0, ss=0):
        super().__init__(hh, mm, ss)
        self.alarm_hh = 0
        self.alarm_mm = 0
        self.alarm_ss = 0
        self.alarm_on_off = False
    
    def setAlarmTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s
    
    def alarm_on(self):
        self.alarm_on_off = True
    
    def alarm_off(self):
        self.alarm_on_off = False
    
    def run(self, label):
        super().run(label)
        if self.alarm_on_off and self.h == self.alarm_hh and self.m == self.alarm_mm and self.s == self.alarm_ss:
            label.config(text="Alarmmm!")
            self.stop()

# Create a tkinter window
root = Tk()
root.title("Clock and Alarm")

# Create a label to display the time
time_label = Label(root, font=("Helvetica", 48))
time_label.pack(pady=20)

# Initialize and run the AlarmClock
a = AlarmClock(0, 0, 0)
a.setAlarmTime(0, 0, 5)
a.alarm_on()
a.run(time_label)

# Start the tkinter main loop
root.mainloop()

#Q2-----------------------------------------------------------------------------------------------------------------

import turtle
import math

def RobotBattle():
    robotList = [];
    turtle.speed(0)
    while True:
        turtle.clear()
        for robot in robotList:
            robot.draw()

        print("==== Robots ====")
        i=0
        for robot in robotList:
            print(i, " : ", )
            robot.displayStatus()
            i += 1
        print("================")

        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            if len(robotList) >= 1:    
                n = int(choice)
                robotList[n].command(robotList)
            else:
                print("Create Some Robot")
                continue
        i = 0
        for robot in robotList:
            if (robot.health <= 0):
                del robotList[i]
            i += 1
    
    # turtle.done()
            


class Robot(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.health = 100
        self.energy = 100
    def move(self, x, y):
        if self.energy - 10 >= 0:
            self.energy -= 10
            self.x = x
            self.y = y
    def draw(self):
        self.dw = turtle.Turtle()
        self.dw.speed(0)
        self.dw.penup()
        self.dw.goto(self.x,self.y)
        self.dw.pendown()
        self.dw.circle(50)
    def displayStatus(self):
        print(f"x= {self.x}, y= {self.y}, health= {self.health}, energy= {self.energy}")
    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()
    def heal(self, r):
        distance = math.sqrt(((r.x - self.x)**2) + ((r.y - self.y)**2))
        if self.energy >= 20 and distance <= 10:
            self.energy -= 20
            r.health += 10
    def command(self, robotList):
        option = input("What you want to action [m-move] [h-heal]: ")
        match option:    
            case "m":
                super().command(robotList)
            case "h":
                rob = int(input("Which robot want to heal: "))
                self.heal(robotList[rob])
            case _:
                print("Not in option")

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5
    def strike(self,r):
        distance = math.sqrt(((r.x - self.x)**2) + ((r.y - self.y)**2))
        if self.energy >= 20 and self.missile > 0 and distance <= 10:
            self.energy -= 20
            self.missile -= 1
            r.health -= 50
        else:
            print("Out-of-range")
    def displayStatus(self):
        print(f"x= {self.x}, y= {self.y}, health= {self.health}, energy= {self.energy}, missile= {self.missile}")
    def command(self, robotList):
        option = input("What you want to action [m-move] [s-strike]: ")
        match option:    
            case "m":
                super().command(robotList)
            case "s":
                rob = int(input("Which robot want to strike: "))
                self.strike(robotList[rob])
            case _:
                print("Not in option")

RobotBattle()

#Q3-----------------------------------------------------------------------------------------------------------------

import turtle

class Point(object):
    def __init__(self):
        self.pt_list = []
        points_input = input("Input pairs of points (x1 y1 x2 y2 ...): ").split()
        for i in range(0, len(points_input), 2):
            x, y = float(points_input[i]), float(points_input[i + 1])
            self.pt_list.append((x, y))   
    def drawPoints(self):
        for x, y in self.pt_list:
            turtle.penup()
            turtle.goto(x,y)
            turtle.dot(5)

class Rectangle2D(Point):
    def __init__(self):
        super().__init__()
        self.drawPoints()
        self.getRectangle()

    def getRectangle(self):
        x_coords = [point[0] for point in self.pt_list]
        y_coords = [point[1] for point in self.pt_list]
        self.x_min = min(x_coords)
        self.x_max = max(x_coords)
        self.y_min = min(y_coords)
        self.y_max = max(y_coords)
        self.width = self.x_max - self.x_min
        self.height = self.y_max - self.y_min
        
        centre_x = (self.x_max + self.x_min)/2
        centre_y = (self.y_max + self.y_min)/2
        
        turtle.penup()
        turtle.goto(self.x_min, self.y_min)
        turtle.pendown()
        for _ in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)
        print(f"The bonding rectangle is center at ({centre_x}, {centre_y}) with width {self.width} and height {self.height}")

c = Rectangle2D()
turtle.done()

#Q1.1 Abstact-----------------------------------------------------------------------------------------------------------------

from abc import ABC,abstractmethod
import turtle

class Char(ABC):
    @abstractmethod
    def draw(self, x, y):
        pass
    @abstractmethod
    def getWidth(self):
        pass
    
class Char0(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.pensize(5)
        for i in range(2):
            turtle.fd(25)
            turtle.right(90)
            turtle.fd(50)
            turtle.right(90)
    def getWidth(self):
        return 50

class Char1(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.fd(25)
        turtle.pendown()
        turtle.pensize(5)
        turtle.right(90)
        turtle.fd(50)
    def getWidth(self):
        return 50

class Char2(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.pensize(5)
        # turtle.left(90)
        # turtle.fd(25)
        # turtle.right(90)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(25)
        turtle.left(90)
        turtle.fd(25)
        turtle.left(90)
        turtle.fd(25)
    def getWidth(self):
        return 50
class Char3(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.pensize(5)
        for i in range(2):
            turtle.fd(25)
            turtle.right(90)
            turtle.fd(25)
            turtle.right(90)
            turtle.fd(25)
            turtle.left(180)
    def getWidth(self):
        return 50
    
class Char4(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.pensize(5)
        turtle.right(90)
        turtle.fd(25)
        turtle.left(90)
        turtle.fd(25)
        turtle.left(90)
        turtle.fd(25)
        turtle.backward(50)
    def getWidth(self):
        return 50

class Char5(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.pensize(5)
        turtle.fd(25)
        turtle.backward(25)
        turtle.right(90)
        turtle.fd(25)
        turtle.left(90)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(25)
    def getWidth(self):
        return 50

class Char6(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.fd(25)
        turtle.right(180)
        turtle.pendown()
        turtle.pensize(5)
        turtle.fd(25)
        turtle.left(90)
        turtle.fd(50)
        turtle.left(90)
        for i in range(3):    
            turtle.fd(25)
            turtle.left(90)
        
    def getWidth(self):
        return 50
    
class Char7(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.pensize(5)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(50)
    def getWidth(self):
        return 50
    
class Char8(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.pensize(5)
        for i in range(4):
            turtle.fd(25)
            turtle.right(90)
        turtle.right(90)
        turtle.fd(25)
        turtle.left(90)
        for i in range(4):
            turtle.fd(25)
            turtle.right(90)
    def getWidth(self):
        return 50

class Char9(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.pensize(5)
        for i in range(4):
            turtle.fd(25)
            turtle.right(90)
        turtle.fd(25)
        turtle.right(90)
        turtle.fd(50)
    def getWidth(self):
        return 50
    
def drawNum(x):
    char_obj = {'0':Char0, '1':Char1, '2':Char2, '3':Char3, '4':Char4, '5':Char5, '6':Char6, '7':Char7, '8':Char8, '9':Char9}

    if isinstance(x, int):
        x = str(x)
    
    turtle.speed(0)  
    x_position = -100    
    y_position = 20
    for i in x:
        char_object = char_obj.get(i)
        if char_object:
            char_object.draw(char_object,x_position, y_position)
            turtle.seth(0)
            x_position += char_object.getWidth(char_object) + 20  
        else:
            print(f"Invalid digit: {i}")

turtle_screen = turtle.Screen()
drawNum(1234567890)
turtle_screen.exitonclick()

#Q2 Polymorphism-----------------------------------------------------------------------------------------------------------------

class StationaryGood(object):
    def price(self,item):
        price = 0 * item
        return price

class Magazine(StationaryGood):
    def price(self,item):
        price = item * 70
        return price

class Book(StationaryGood):
    def price(self, item):
        price = item * 90
        return price

class Ribbon(StationaryGood):
    def price(self, item):
        price = item * 5
        return price
        

basket = {Magazine():3, Book():2, Ribbon():10}

def getTotalCost(basket):
    totalcost = 0
    for item, quantity in basket.items():
        totalcost += item.price(quantity)
    return totalcost


cost = getTotalCost(basket)
print("Total cost: ", cost)
