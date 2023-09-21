import turtle

sq = turtle.Turtle()
window = turtle.Screen()

sq.speed(0)
def one(width):
    for i in range(4):
        sq.fd(width)
        sq.left(90)

def second(width):
    for i in range(4):
        for k in range(1,5):
            one(width*k)
        sq.left(90)

second(20)

turtle.done()