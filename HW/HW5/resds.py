# # # import turtle

# # # c = turtle.Turtle()
# # # wind = turtle.Screen()

# # # c.speed("fast")
# # # month = 1

# # # while month <= 12:
# # #     if month == 2:
# # #         days_in_month = 29
# # #     elif month in [4, 6, 9, 11]:
# # #         days_in_month = 30
# # #     else:
# # #         days_in_month = 31
    
# # #     # Head
# # #     c.forward(210)
# # #     c.left(90)
# # #     c.forward(20)
# # #     c.left(90)
# # #     c.forward(210)
# # #     c.left(90)
# # #     c.forward(20)

# # #     # Day block
# # #     x = 0
# # #     y = 0
# # #     c.penup() 
# # #     c.goto(x + 5, y)  # Move to write position
# # #     c.write(f"Month#{month}", font=('arial', 9, 'normal'), align='left')
# # #     c.goto(x, y)
# # #     c.pendown()
# # #     c.forward(20)
# # #     c.left(90)
    
# # #     day_names = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    
# # #     for day_name in day_names:
# # #         c.write(day_name, font=('arial', 9, 'normal'), align='center')
# # #         c.forward(210 / 7)
# # #         c.left(90)
# # #         c.forward(20)
# # #         c.back(20)
# # #         c.right(90)
    
# # #     # Loop for drawing rows
# # #     for week in range(1, 7):
# # #         c.penup()
# # #         c.goto(x, y - (20 * week))
# # #         c.pendown()
# # #         c.right(90)
# # #         c.forward(20)
# # #         c.left(90)
        
# # #         for day_num in range(7):
# # #             day_value = (week - 1) * 7 + day_num + 1
# # #             if day_value <= days_in_month:
# # #                 c.write(day_value, font=('arial', 9, 'normal'), align='center')
# # #             c.forward(210 / 7)
# # #             c.left(90)
# # #             c.forward(20)
# # #             c.back(20)
# # #             c.right(90)
    
# # #     # Move to the next month
# # #     c.penup()
# # #     c.goto(x + 210 + 20, y)  # Move to the start of next month
# # #     c.pendown()
    
# # #     month += 1

# # # turtle.done()

# # # # import turtle

# # # # c = turtle.Turtle()
# # # # wind = turtle.Screen()

# # # # c.speed("fastest")
# # # # month = 1
# # # # while month <= 12:  # <= 12
# # # #     if month == 2:
# # # #         days_in_month = 29
# # # #     elif month in [4, 6, 9, 11]:
# # # #         days_in_month = 30
# # # #     else:
# # # #         days_in_month = 31
    
# # # #     # ... (previous code)

# # # #     # Day block
# # # #     x = 0
# # # #     y = 0
# # # #     c.penup() 
# # # #     c.goto(x + 5, y)  # Move to write position
# # # #     c.write(f"Month#{month}", font=('arial', 9, 'normal'), align='left')
# # # #     c.goto(x, y)
# # # #     c.pendown()
# # # #     c.forward(20)
# # # #     c.left(90)
# # # #     week = 0
# # # #     day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    
# # # #     while week < 7:  # for printing row
# # # #         d = 0
# # # #         dim = 0  # Initialize dim inside the week loop
# # # #         while d < 7:  # week and day
# # # #             if week == 0:
# # # #                 c.write(day[d], font=('arial', 9, 'normal'), align='left')
# # # #             else:
# # # #                 if dim < days_in_month:
# # # #                     dim += 1
# # # #                     c.write(dim, font=('arial', 9, 'normal'), align='left')
# # # #                 else:
# # # #                     break  # Stop if days exceed days_in_month
# # # #             c.forward(210/7)
# # # #             c.left(90)
# # # #             c.forward(20)
# # # #             c.back(20)
# # # #             c.right(90)
# # # #             d += 1
# # # #         c.penup()
# # # #         week += 1
# # # #         c.goto(x, y - (20 * week))
# # # #         c.pendown()
# # # #         c.right(90)
# # # #         c.forward(20)
# # # #         c.left(90)

# # # #     # loop row1 
# # # #     c.forward(210/7)
# # # #     c.left(90)
# # # #     c.forward(20)
# # # #     c.back(20)
# # # #     c.right(90)

# # # #     month += 1

# # # # turtle.done()

# # # # import turtle

# # # # c = turtle.Turtle()
# # # # wind = turtle.Screen()

# # # # c.speed("fastest")

# # # # for month in range(1, 13):  # Loop through all twelve months
# # # #     if month == 2:
# # # #         days_in_month = 29
# # # #     elif month in [4, 6, 9, 11]:
# # # #         days_in_month = 30
# # # #     else:
# # # #         days_in_month = 31

# # # #     # Head
# # # #     c.forward(210)
# # # #     c.left(90)
# # # #     c.forward(20)
# # # #     c.left(90)
# # # #     c.forward(210)
# # # #     c.left(90)
# # # #     c.forward(20)

# # # #     # Day block
# # # #     x = 0
# # # #     y = 0
# # # #     c.penup()
# # # #     c.goto(x + 5, y)  # for write
# # # #     c.write(f"Month#{month}", font=('arial', 9, 'normal'), align='left')
# # # #     c.goto(x, y)
# # # #     c.pendown()
# # # #     c.forward(20)
# # # #     c.left(90)
# # # #     week = 0
# # # #     dim = 0
# # # #     day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
# # # #     while week < 7:  # for printing row
# # # #         d = 0
# # # #         while d < 7:  # week and day
# # # #             if week == 0:
# # # #                 c.write(day[d], font=('arial', 9, 'normal'), align='left')
# # # #             else:
# # # #                 if dim < days_in_month:
# # # #                     dim += 1
# # # #                     c.write(dim, font=('arial', 9, 'normal'), align='left')
# # # #                 else:
# # # #                     continue

# # # #             c.forward(210 / 7)
# # # #             c.left(90)
# # # #             c.forward(20)
# # # #             c.back(20)
# # # #             c.right(90)
# # # #             d += 1
# # # #         c.penup()
# # # #         week += 1
# # # #         c.goto(x, y - (20 * week))
# # # #         c.pendown()
# # # #         c.right(90)
# # # #         c.forward(20)
# # # #         c.left(90)

# # # #     # Loop row1
# # # #     c.forward(210 / 7)
# # # #     c.left(90)
# # # #     c.forward(20)
# # # #     c.back(20)
# # # #     c.right(90)

# # # # turtle.done()

# # import turtle

# # x = 0
# # y = 0

# # c = turtle.Turtle()
# # wind = turtle.Screen()

# # c.speed("fastest")
# # month = 1
# # previous_last_day_weekday = 0  # Initialize the weekday of the last day of the previous month

# # while month <= 12:
# #     if month == 2:
# #         days_in_month = 29
# #     elif month in [4, 6, 9, 11]:
# #         days_in_month = 30
# #     else:
# #         days_in_month = 31

# #     # Calculate the starting day for the current month
# #     starting_day = (previous_last_day_weekday + 1) % 7

# #     # Head
# #     c.forward(210)
# #     c.left(90)
# #     c.forward(20)
# #     c.left(90)
# #     c.forward(210)
# #     c.left(90)
# #     c.forward(20)

# #     # Day block
# #     c.penup()
# #     c.goto(x + 5, y)  # for write
# #     c.write(f"Month#{month}", font=('arial', 9, 'normal'), align='left')
# #     c.goto(x, y)
# #     c.pendown()
# #     c.forward(20)
# #     c.left(90)
# #     week = 0
# #     dim = 0
# #     day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
# #     for _ in range(starting_day):
# #         c.forward(210 / 7)
# #         c.left(90)
# #         c.forward(20)
# #         c.back(20)
# #         c.right(90)

# #     while week < 7:  # for printing row
# #         d = starting_day
# #         while d < 7:  # week and day
# #             if week == 0:
# #                 c.write(day[d], font=('arial', 9, 'normal'), align='left')
# #             else:
# #                 if dim < days_in_month:
# #                     dim += 1
# #                     c.write(dim, font=('arial', 9, 'normal'), align='left')

# #             c.forward(210 / 7)
# #             c.left(90)
# #             c.forward(20)
# #             c.back(20)
# #             c.right(90)
# #             d += 1
# #         c.penup()
# #         week += 1
# #         c.goto(x, y - (20 * week))
# #         c.pendown()
# #         c.right(90)
# #         c.forward(20)
# #         c.left(90)

# #     # Loop row1
# #     c.forward(210 / 7)
# #     c.left(90)
# #     c.forward(20)
# #     c.back(20)
# #     c.right(90)

# #     month += 1
# #     # next month
# #     c.penup()
# #     y = -160
# #     c.goto(x, y)
# #     c.pendown()

# #     # Calculate the weekday of the last day of the current month
# #     previous_last_day_weekday = (starting_day + days_in_month - 1) % 7

# # turtle.done()

# import turtle

# x = 0
# y = 0

# c = turtle.Turtle()
# wind = turtle.Screen()

# c.speed("fastest")
# month = 1
# previous_last_day_weekday = 0  # Initialize the weekday of the last day of the previous month

# while month <= 12:
#     if month == 2:
#         days_in_month = 29
#     elif month in [4, 6, 9, 11]:
#         days_in_month = 30
#     else:
#         days_in_month = 31

#     # Calculate the starting day for the current month
#     starting_day = (previous_last_day_weekday + 1) % 7

#     # Head
#     c.forward(210)
#     c.left(90)
#     c.forward(20)
#     c.left(90)
#     c.forward(210)
#     c.left(90)
#     c.forward(20)

#     # Day block
#     c.penup()
#     c.goto(x + 5, y)  # for write
#     c.write(f"Month#{month}", font=('arial', 9, 'normal'), align='left')
#     c.goto(x, y)
#     c.pendown()

#     week = 0
#     dim = 0
#     day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
#     for _ in range(starting_day):
#         c.write(" ", font=('arial', 9, 'normal'), align='left')
#         c.forward(210 / 7)
#         c.left(90)
#         c.forward(20)
#         c.back(20)
#         c.right(90)

#     while week < 7:  # for printing row
#         d = starting_day
#         while d < 7:  # week and day
#             if week == 0:
#                 c.write(day[d], font=('arial', 9, 'normal'), align='left')
#             else:
#                 if dim < days_in_month:
#                     dim += 1
#                     c.write(dim, font=('arial', 9, 'normal'), align='left')

#             c.forward(210 / 7)
#             c.left(90)
#             c.forward(20)
#             c.back(20)
#             c.right(90)
#             d += 1
#         c.penup()
#         week += 1
#         c.goto(x, y - (20 * week))
#         c.pendown()
#         c.right(90)
#         c.forward(20)
#         c.left(90)

#     # Loop row1
#     c.forward(210 / 7)
#     c.left(90)
#     c.forward(20)
#     c.back(20)
#     c.right(90)

#     month += 1
#     # next month
#     c.penup()
#     y = -160
#     c.goto(x, y)
#     c.pendown()

#     # Calculate the weekday of the last day of the current month
#     previous_last_day_weekday = (starting_day + days_in_month - 1) % 7

# turtle.done()

import turtle

x = -450  # Initial x position for the calendar
y = 300   # Initial y position for the calendar

c = turtle.Turtle()
wind = turtle.Screen()

c.speed("fastest")

# Loop for each month
for month in range(1, 13):
    if month == 2:
        days_in_month = 29
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    else:
        days_in_month = 31

    # Head
    c.penup()
    c.goto(x, y)
    c.write(f"Month#{month}", font=('arial', 14, 'bold'), align='center')
    c.forward(150)
    c.pendown()

    # Days of the week
    days = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    for day in days:
        c.penup()
        c.goto(x, y - 30)
        c.write(day, font=('arial', 10, 'normal'), align='center')
        c.forward(100)

    c.penup()
    c.goto(x, y - 60)
    c.pendown()

    # Generate the calendar grid
    day_num = 1
    for week in range(6):
        for _ in range(7):
            if day_num <= days_in_month:
                c.write(str(day_num), font=('arial', 10, 'normal'), align='center')
            c.forward(100)
            day_num += 1
        c.penup()
        c.goto(x, y - 60 - (week + 1) * 30)
        c.pendown()

    x += 750  # Move to the next month
    if month % 3 == 0:
        x = -450
        y -= 250

turtle.done()
