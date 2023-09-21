def time24hourTo12hour(time):
    a, b = time.split(":")
    a = int(a)
    if a > 12:
        a -= 12
        dt = "PM."
    elif a == 12:
        dt = "PM."
    elif a == 0:
        a += 12
        dt = "AM."
    else:
        dt = "AM."
    new_time = str(a) + ":" + b + " " + dt #sum it together to get a string of time
    return new_time
ip = (input("enter the time in24hour: "))
print(time24hourTo12hour(ip))