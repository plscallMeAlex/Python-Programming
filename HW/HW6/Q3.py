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
