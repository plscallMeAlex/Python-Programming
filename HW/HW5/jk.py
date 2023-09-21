import turtle

x = 0
y = 0
fd = 0

c = turtle.Turtle()
wind = turtle.Screen()
wind.screensize(2000, 10000)

c.speed("fastest")
month = 1
while month <= 12:
    if month == 2:
        days_in_month = 28
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    else:
        days_in_month = 31

    # Print month header
    c.penup()
    c.goto(x + 5, y + 210)
    c.write(f"Month #{month}", font=('arial', 9, 'normal'), align='left')
    c.goto(x, y)
    c.pendown()

    # Calculate the first day of the week (fd) for the current month
    if month == 1:
        fd = 0  # Start with Sunday for the first month
    else:
        fd = (fd + days_in_prev_month) % 7

    # Print day headers
    day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    for d in day:
        c.write(d, font=('arial', 9, 'normal'), align='left')
        c.forward(210 / 7)

    c.backward(210)
    c.left(90)
    c.forward(20)
    c.right(90)

    week = 0
    dim = 0

    while dim < days_in_month:
        if week == 0:
            c.penup()
            c.goto(x, y - (20 * (week + 1)))
            c.pendown()

        for d in range(7):
            if week == 0 and d < fd:
                c.write("", font=('arial', 9, 'normal'), align='left')
            elif dim < days_in_month:
                dim += 1
                c.write(dim, font=('arial', 9, 'normal'), align='left')

            c.forward(210 / 7)

        c.backward(210)
        c.left(90)
        c.forward(20)
        c.right(90)

        week += 1

    days_in_prev_month = days_in_month

    y -= (20 * week) + 60
    month += 1

# Exit the turtle graphics window
turtle.done()
