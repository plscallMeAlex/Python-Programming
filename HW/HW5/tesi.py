import turtle

x=0
y=0

c = turtle.Turtle()
wind = turtle.Screen()
wind.screensize(2000, 10000)

c.speed("fastest")
month = 1
while month <= 12: #<= 12
    if month == 2:
        days_in_month = 28
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    else:
        days_in_month = 31
    #head
    c.forward(210)
    c.left(90)
    c.forward(20)
    c.left(90)
    c.forward(210)
    c.left(90)
    c.forward(20)

    #day block
    c.penup() 
    c.goto(x+5,y)#for write
    c.write(f"Month#{month}", font=('arial', 9, 'normal'), align='left')
    c.goto(x,y)
    c.pendown()
    c.forward(20)
    c.left(90)

    if month == 1:
        fd = 0
    else:
        fd = (fd + previous_month) %7
    week = 0
    dim = 0
    day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    while week < 7:#for printing week
        d = 0
        while d < 7: #for day in each line
            if week == 0:
                c.write(day[d], font=('arial', 9, 'normal'), align='left')
            else:
                # if dim == days_in_month:
                #     for a in range(7):
                #         if fd == d:
                #             fd = a
                #             break
                #         else: fd = a
                if dim < days_in_month:
                    if week == 1 and d < fd:
                        c.write("",align="left")
                    if week >= 1 and d >= fd:
                        dim += 1 #printing day until it is correct
                        c.write(dim, font=('arial', 9, 'normal'), align='left')
                    # elif week == 1 and d > fd:
                    #     dim += 1
                    #     c.write(dim, font=('arial', 9, 'normal'), align='left')
                    #     pass
                    elif week > 1:
                        dim += 1
                        c.write(dim, font=('arial', 9, 'normal'), align='left')
                    #     pass
                    # elif week == 1 and d != fd and dim == 0:
                    #     pass
                    # elif week >= 1 or d > fd:
                    #     dim += 1
                    #     c.write(dim, font=('arial', 9, 'normal'), align='left')
                    #     pass
                        # dim += 1 #printing day until it is correct
                        # c.write(dim, font=('arial', 9, 'normal'), align='left')
            # if dim == days_in_month:
            #     fd = 0
            #     for a in range(7):
            #         if fd == d:
            #             break
            #         else: fd += 1
            # else: pass #finding first day in next month   
            d += 1       
            if d == 7 and dim == days_in_month: break  #exit loop in the last week
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
    y -= (20*week) + 60
    previous_month = days_in_month
    month += 1
    #next month
    c.penup()
    c.goto(x, y)
    c.pendown()

turtle.done()

