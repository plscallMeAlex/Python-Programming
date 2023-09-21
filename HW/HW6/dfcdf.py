import turtle
move = turtle.Turtle()

day_month = [0, 31, 28, 31, 30, 31, 30, 31, 13, 30, 31, 30, 31]
name_month = ["", "January", "February", "March", "April", "May", "June", 
"July", "August", "September", "October", "November", "December"]
day_week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
x = y = 0

def calendar_of_2023(month): #main function
    fd = 6
    move.speed("fastest")
    month_name_box(month)
    each_week(month,fd)
    window = turtle.Screen()
    move.hideturtle()
 
def month_name_box(month): #for long rectangle store name of the month
    move.forward(210)
    move.left(90)
    move.forward(20)
    move.left(90)
    move.forward(210)
    move.left(90)
    move.forward(20)
    move.penup()
    move.goto(x+67,y)
    move.write(name_month[month] + " 2023", font=('arial', 9, 'normal'), align='left')
    move.goto(x,y)
    move.pendown()
 
def each_week(month,fd): #function that draw and write a day 
    if month == 1:
        fd = 6 #because this year first month start at sunday
    else: 
        for i in range(0,month):
            fd = ((fd + day_month[i]) % 7)
    dim = 0
    week = 0
    move.fd(20)
    move.left(90)
    while week < 7: 
        d = 0
        while d < 7:
            if week == 0:
                move.penup()
                move.setx((d*30)+7)
                move.write(day_week[d], font=('arial', 9, 'normal'), align='left')
                move.setx((d*30))
                move.pendown()
            else:
                if dim < day_month[month]:
                    if week == 1 and d < fd:
                        move.write("")
                    if week >= 1 and d>= fd:
                        dim += 1
                        move.penup()
                        if dim < 10: #for writing a number in the middle of a box
                            move.setx((d*30)+11)
                        else:
                            move.setx((d*30)+7)
                        move.write(dim, font=('arial', 9, 'normal'), align='left')
                        move.setx((d*30))
                        move.pendown() 
                    elif week > 1:
                        dim += 1
                        move.penup()
                        if dim < 10: #for writing a number in the middle of a box
                            move.setx((d*30)+11)
                        else:
                            move.setx((d*30)+7)
                        move.write(dim, font=('arial', 9, 'normal'), align='left')
                        move.setx((d*30))
                        move.pendown()
            d += 1
            if d == 7 and dim == day_month[month]: break
            move.fd(30)
            move.left(90)
            move.fd(20)
            move.back(20)
            move.right(90)
        if d == 7 and dim == day_month[month]: break
        move.penup()
        week += 1
        move.goto(x,y-(week*20))
        move.pendown()
        move.right(90)
        move.fd(20)
        move.left(90)
    move.forward(30)
    move.left(90)
    move.fd(20)
    move.back(20)
    move.right(90)

calendar_of_2023(8)
turtle.done()