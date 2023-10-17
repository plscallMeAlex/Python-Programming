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