n = eval(input("Enter number what you what to find a square root: "))
guess = n/2

for i in range(8):
    temp = n/guess
    guess =(guess + temp)/2
    if i == 5:
        print(f"{round(guess,3)}")
    if i == 6:
        print(f"{round(guess,3)}")
    if i == 7:
        print(f"{round(guess,3)}")

