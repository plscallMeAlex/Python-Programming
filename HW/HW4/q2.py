import turtle

x1,y1 = eval(input("Center Square of square1: "))
w1,h1 = eval(input("Width / Height square1: "))
x2,y2 = eval(input("Center Square of square2: "))
w2,h2 = eval(input("Width / Height square1: "))

x1_left = x1-w1/2
x1_right = x1+w1/2
y1_up = y1+h1/2
y1_down = y1-h1/2

x2_left = x2-w2/2
x2_right = x2+w2/2
y2_up = y2+h2/2
y2_down = y2-h2/2

if ((x1_right <= x2_left) or (x2_right <= x1_left)): #not colab 2 pattern right left
    result = "non overlap"
    print(result)
elif (y1_down >= y2_up) or (y2_down >= y1_up): #non overlap 2 pattern up down
    result = "non overlap"
    print(result)
elif (x1 == x2 and y1 == y2) and (w1 == w2 and h1 == h2): #same rectangle overwrite to the first draw
    result = "overwrite_shape"
    print(result)
elif ((x1_left >= x2_left) and (x1_right <= x2_right)) and ((y1_up <= y2_up) and (y1_down >= y2_down)): #when first rec in the second rec
    result = "inside"
    print(result)
elif ((x2_left >= x1_left) and (x2_right <= x1_right)) and ((y2_up <= y1_up) and (y2_down >= y1_down)): #when second rec in the first rec
    result = "inside"
    print(result)
elif ((x1_left >= x2_left) and (x2_right >= x1_right)) and ((y1_up > y2_up) and (y2_down > y1_down)): #condition when it cross each other which it is a another kind of lap 
    result = "cross"
    print(result)
elif ((x2_left >= x1_left) and (x1_right >= x2_right)) and ((y2_up > y1_up) and (y1_down > y2_down)): #cross condition
    result = "cross"
    print(result)
elif (x2_left < x1_right) and ((y1_up != y2_down) or (y2_up != y1_down)): #when second rec is on above first rec
    result = "overlap"
    print(result)
elif (x1_left < x2_right) and ((y1_up != y2_down) or (y2_up != y1_down)): #when first rec is on above second rec
    result = "overlap"
    print(result)
else:
    print("no")



re = turtle.Turtle()
window = turtle.Screen()

re.speed(10)
re.penup()
re.goto(x1,y1)
re.write("({},{})".format(x1,y1))
re.goto(x1+w1/2, y1+h1/2)
re.right(180)
re.pendown()
re.forward(w1)
re.left(90)
re.forward(h1)
re.left(90)
re.forward(w1)
re.left(90)
re.forward(h1)
re.penup()
re.goto(x2,y2)
re.write("({},{})".format(x2,y2))
re.goto(x2+w2/2,y2+h2/2)
re.pendown()
re.left(90)
re.forward(w2)
re.left(90)
re.forward(h2)
re.left(90)
re.forward(w2)
re.left(90)
re.forward(h2)
re.hideturtle()


turtle.done()