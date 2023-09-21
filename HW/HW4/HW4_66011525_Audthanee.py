#------------------------------------------------------------------------
#Problem.1
import math
import turtle
x0,y0 = eval(input("Point0: "))
x1,y1 = eval(input("Point1: "))
x2,y2 = eval(input("Point2: "))

if x0 == x1:
    m = "inf"
else:
    m = (y1-y0)/(x1-x0)
#check if it is a vertical line

my_list_x = []
my_list_x.append(x0)
my_list_x.append(x1)
my_list_y = []
my_list_y.append(y0)
my_list_y.append(y1)

less_than = min(my_list_x)
more_than = max(my_list_x)
upperer = max(my_list_y)
lowerer = min(my_list_y)

def error(): #for return else condition to 0 fix error
    return 0

if m != 0: #filter m = 0 because it can't divided by zero
    x_in_line = ((y2-y0)/m) + x0 #find x in the line at same level y of p2
    y_in_line = (m*(y2-x0)) + y0 #find y in the line at same level x of p2

if m == "inf": #line-pattern1:Vertical
    if x2 > x0:
        result = "right"
        print(result)
    elif x2 < x0:
        result = "left"
        print(result)
    else:
        print("same_line")
elif m == 0: #line-pattern2:Horizontal
    if y2 > x0:
        result = "upper"
        print(result)
    elif y2 < x0:
        result = "lower"
        print(result)
    else:
        result = "same_line"
        print(result)
elif m > 0: #line go up to the right
    if x2 < less_than:#outside of line 
        result = "left"
        print(result)
    elif x2 > more_than:#outside of line 
        result = "right"
        print(result)
    elif x2 in range(less_than, more_than) and (y2 > lowerer and y2 < upperer): #in the range of line 
        if x_in_line-x2 > 0: #check difference between point2 and point in the line at the same y
            result = "left"
            print(result)
        elif x2-x_in_line > 0: #check difference between point2 and point in the line at the same y
            result = "right"
            print(result)
        else:
            result = "in the line"
            print(result)
    elif x2 in range(less_than, more_than) and (y2 < lowerer or y2 > upperer): #in the range of line but in will be up and down 
        if y_in_line - y2 > 0: #check the difference between p2 and point in the line at the same x
            result = "upper"
            print(result)
        elif y2 - y_in_line > 0: #check the difference between p2 and point in the line at the same x
            result = "lower"
            print(result)
        else:
            result = "in the line"
            print(result)
elif m < 0:
    if x2 < less_than:#outside of line 
        result = "left"
        print(result)
    elif x2 > more_than:#outside of line 
        result = "right"
        print(result)
    elif x2 in range(less_than, more_than) and (y2 > lowerer and y2 < upperer): #in the range of line 
        if x_in_line-x2 > 0: #check difference between point2 and point in the line at the same y
            result = "left"
            print(result)
        elif x2-x_in_line > 0: #check difference between point2 and point in the line at the same y
            result = "right"
            print(result)
        else:
            result = "in the line"
            print(result)
    elif x2 in range(less_than, more_than) and (y2 < lowerer or y2 > upperer): #in the range of line but in will be up and down 
        if y_in_line - y2 > 0: #check the difference between p2 and point in the line at the same x
            result = "upper"
            print(result)
        elif y2 - y_in_line > 0: #check the difference between p2 and point in the line at the same x
            result = "lower"
            print(result)
        else:
            result = "in the line"
            print(result)

window = turtle.Screen()
p = turtle.Turtle()

p.penup()
p.goto(x0, y0)
p.write("P0")
p.pendown()
p.goto(x1, y1)
p.write("P1")
p.penup()
p.goto(x2,y2)
p.pendown()
p.write("P2\n")
p.write(result)

turtle.done()
#------------------------------------------------------------------------
#Problem.2
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