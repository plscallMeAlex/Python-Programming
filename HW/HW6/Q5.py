def reverse(num):
    new_num = 0
    while num != 0:
        new_num = new_num*10 + num%10 #get the last digit and then add to the new var if it the second loop it will multiply it with 10 to store another digit
        num = num//10 #the digit of number that is argument will decrease
    return new_num

print(f"{3467}:{reverse(3467)}")