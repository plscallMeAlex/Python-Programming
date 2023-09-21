import turtle

x=0
y=0

c = turtle.Turtle()
wind = turtle.Screen()
wind.screensize(2000, 10000)

c.speed("fast")
month = 1
while month <= 12: 
    if month == 2:
        days_in_month = 28
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    else:
        days_in_month = 31
    #head <display month>
    c.forward(210)
    c.left(90)
    c.forward(20)
    c.left(90)
    c.forward(210)
    c.left(90)
    c.forward(20)

    #Block Day 
    c.penup() 
    c.goto(x+5,y)#for writing space
    c.write(f"Month#{month}", font=('arial', 9, 'normal'), align='left')
    c.goto(x,y)
    c.pendown()
    c.forward(20)
    c.left(90)

    if month == 1:
        fd = 0
    else:
        fd = (fd + previous_month) %7#finding which column to start
    week = 0
    dim = 0
    day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    while week < 7:#for printing week
        d = 0
        while d < 7: #for day in each line
            if week == 0:
                c.penup()
                c.setx((d*30)+7)
                c.write(day[d], font=('arial', 9, 'normal'), align='left')
                c.setx((d*30))
                c.pendown()
            else:
                if dim < days_in_month:
                    if week == 1 and d < fd:#if the column not the same as 
                        c.write("",align="left")#print nothing before printing first day of the month
                    if week >= 1 and d >= fd:
                        dim += 1 #printing day
                        c.penup()
                        if dim < 10: #for writing a number in the middle of a box
                            c.setx((d*30)+11)
                        else:
                            c.setx((d*30)+7)
                        c.write(dim, font=('arial', 9, 'normal'), align='left')
                        c.setx((d*30))
                        c.pendown()
                    elif week > 1:
                        dim += 1
                        c.penup()
                        if dim < 10: #for writing a number in the middle of a box
                            c.setx((d*30)+11)
                        else:
                            c.setx((d*30)+7)
                        c.write(dim, font=('arial', 9, 'normal'), align='left')
                        c.setx((d*30))
                        c.pendown()  
            d += 1       
            if d == 7 and dim == days_in_month: break  #exit loop in the last week because it print more than needed
            c.forward(210/7)
            c.left(90)
            c.forward(20)
            c.back(20)
            c.right(90) 
        if d == 7 and dim == days_in_month: break
        c.penup()
        week += 1
        c.goto(x,y-(20*week))
        c.pendown()
        c.right(90)
        c.forward(20)
        c.left(90)

    # loop row1 
    c.forward(210/7)
    c.left(90)
    c.forward(20)
    c.back(20)
    c.right(90)

    w = week
    y -= (20*week) + 60 #distance between the month
    previous_month = days_in_month #set for begining checking the last day of the month
    month += 1
    #next month
    c.penup()
    c.goto(x, y)
    c.pendown()


turtle.done()

