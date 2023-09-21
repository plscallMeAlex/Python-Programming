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
