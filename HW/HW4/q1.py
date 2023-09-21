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