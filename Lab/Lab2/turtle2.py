import turtle

pi = 3.14159265
x = int(input("X position:"))
y = int(input("Y position:"))
rad = int(input("Grant me radius:"))
area = rad*rad*pi

window = turtle.Screen()
cir = turtle.Turtle()
cir.penup()
cir.setpos(x, y)
cir.pos()
cir.pendown()
cir.right(90)
cir.penup()
cir.forward(rad)
cir.pendown()
cir.circle(rad)
cir.hideturtle()
cir.left(90)
cir.penup()
cir.forward(rad)
cir.pendown()
cir.write(area)

turtle.done()