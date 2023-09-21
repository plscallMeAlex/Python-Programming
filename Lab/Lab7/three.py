from turtle import *
from math import pi
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def getArea(self):
        area = self.width * self.height
        print(f"Area: {area}")
    def getPerimeter(self):
        perm = 2*(self.width+self.height)
        print(f"Perimeter: {perm}")
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    def draw(self):
        penup()
        goto(self.x, self.y)
        pendown()
        for i in range(2):
            forward(self.width)
            right(90)
            forward(self.height)
            right(90)
    def intersect(self, rec):
        p1 = [self.x - self.width/2, self.y + self.height/2]
        p2 = [self.x + self.width/2, self.y + self.height/2] 
        p3 = [self.x + self.width/2, self.y - self.height/2]
        p4 = [self.x - self.width/2, self.y - self.height/2] 
        
        p5 = [rec.x - rec.width/2, rec.y + rec.height/2]
        p6 = [rec.x + rec.width/2, rec.y + rec.height/2] 
        p7 = [rec.x + rec.width/2, rec.y - rec.height/2]
        p8 = [rec.x - rec.width/2, rec.y - rec.height/2] 
        
        if (p1[0] >= p5[0] and p1[1] <= p5[1]) and (p2[0] <= p6[0]) and (p4[1] >= p7[1]):
            return Rectangle(self.x, self.y, self.width, self.height)
        elif (p1[0] <= p5[0] and p1[1] >= p5[1]) and (p2[0] >= p6[0]) and (p4[1] <= p7[1]):
            return Rectangle(rec.x, rec.y, rec.width, rec.height)
        elif ((p6[0] > p1[0]) and (p6[1] > p3[1])) and (p7[1] < p2[1]) and (p5[0] < p2[0]): 
            new_width = min(p2[0], p6[0]) - max(p1[0], p5[0])
            new_height = min(p2[1], p6[1]) - max(p3[1], p7[1])
            return Rectangle(max(p1[0], p5[0]) + new_width/2, max(p3[1], p7[1]) + new_height/2, new_width, new_height)
        else:
            return None

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def getArea(self):
        area = pi*(self.radius**2)
        return area
    def getPerimeter(self):
        perm = 2*pi*self.radius
        return perm
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    def draw(self):
        penup()
        goto(self.x + self.radius, self.y)
        pendown()
        circle(self.radius)
        
a = Rectangle(0, 0, 100, 200)
b = Rectangle(-200,0,100,100)

speed(0)
a.draw()
b.draw()

c = a.intersect(b)

d = Rectangle(-50,-50,200,50)
d.draw()
color("red")
e = a.intersect(d)
e.draw()
e.move(-100,100)
e.draw()

done()