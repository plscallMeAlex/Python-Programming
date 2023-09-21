#Question 1---------------------------------------------------------------------------------
# def time24hourTo12hour(time):
#     a, b = time.split(":")
#     a = int(a)
#     if a > 12:
#         a -= 12
#         dt = "PM."
#     elif a == 12:
#         dt = "PM."
#     elif a == 0:
#         a += 12
#         dt = "AM."
#     else:
#         dt = "AM."
#     new_time = str(a) + ":" + b + " " + dt #sum it together to get a string of time
#     return new_time
# ip = (input("enter the time in24hour: "))
# print(time24hourTo12hour(ip))

#Question 2---------------------------------------------------------------------------------
import turtle
move = turtle.Turtle()

day_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name_month = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
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
    

# calendar_of_2023(1)
# calendar_of_2023(2)
# calendar_of_2023(3)
calendar_of_2023(4)
# calendar_of_2023(5)
# calendar_of_2023(6)
# calendar_of_2023(7)
# calendar_of_2023(8)
# calendar_of_2023(9)
# calendar_of_2023(10)
# calendar_of_2023(11)
#calendar_of_2023(12)

turtle.done()

#Question 3---------------------------------------------------------------------------------
def number_converter(nb):
    if nb == 0:
        return "zero"
    one_digit = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    second_digit_teen = ["ten", "eleven", "twevle", "thirteen", "fourteen", "fiftheen", "sixteen", "seventeen", "eighteen", "nineteen"]
    second_digit_ty = ["", "", "twenty", "thirty", "fourty", "fifthy", "sixty", "seventy", "eighty", "ninety"]
    if nb in range(1,10):
        return one_digit[nb]
    #end with teen
    elif nb in range(10,20):
        return second_digit_teen[nb%10]
    #end with ty
    elif nb in range(20, 100):
        if one_digit[nb%10] == "" :
            return second_digit_ty[nb//10]
        return second_digit_ty[nb//10] + "-" + one_digit[nb%10]
    #from upper 1 hundred
    elif nb in range(100,1000): 
        if nb%100 == 0: #condition for end with hundred
            return one_digit[nb//100] + " hundred"  
        elif nb%100 in range(1,10): #condition that in ten position is zero
            return one_digit[nb//100] + " hundred and " + one_digit[nb%100]
        elif nb%100 in range(10,20): #hundred that end with teen
            return one_digit[nb//100] + " hundred and " + second_digit_teen[(nb%100)%10]
        elif nb%100 in range(20,100): #hundred that endty with digit
            if (nb%100)%10 == 0: #hundred that in ten position have a digit but one position is zero
                return one_digit[nb//100] + " hundred and " + second_digit_ty[(nb%100)//10]

            return one_digit[nb//100] + " hundred and " + second_digit_ty[(nb%100)//10] + "-" + one_digit[(nb%100)%10] #end with ty and end with digit  
    else:
        return "I don't know."

nb = int(input("Enter number: "))
print(f"{number_converter(nb)}")

#Question 4---------------------------------------------------------------------------------
def money_notes(money):
    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    ths = fhd = ohd = ftb = twtb = tb = fb = twb = ob = 0 #declare a counter of bank notes
    va = [ths, fhd, ohd, ftb, twtb, tb, fb, twb, ob] #store into list to make it ease of use
    count = 0 #set for using index of list va and notes
    while money != 0: 
        if money - notes[count] >= 0:
            money -= notes[count]
            va[count] += 1
            continue
        elif money - notes[count] < 0:
            count += 1
            continue
    for i in range(0,9):
        if va[i] == 0:
            continue
        if i < 5:
            print(f"{notes[i]}-Baht notes: {va[i]}")
        else:
            print(f"{notes[i]}-Baht coins: {va[i]}")
            
print("Input your amount of money: ", end='\033[4m') #at the end of text it will start underline
money = int(input("")) #get a input value from user but it promt the user no text
print(end='\033[0m') #end of underline because we need to underline only user input value

money_notes(money) #call function

#Question 5---------------------------------------------------------------------------------
def reverse(num):
    new_num = 0
    while num != 0:
        new_num = new_num*10 + num%10 #get the last digit and then add to the new var if it the second loop it will multiply it with 10 to store another digit
        num = num//10 #the digit of number that is argument will decrease
    return new_num

print(f"{3467}:{reverse(3467)}")