while True: 
    input_value = input("Please enter a character: ")
    if input_value == "\t":
        print("Good bye, see you tomorrow.")
        break
    if len(input_value) == 1 or input_value.isnumeric():
        if ord(input_value) in range(0x30, 0x39+1):
            a = "numeric character"
            print(f">>{input_value} is a {a}.")
        elif ord(input_value) in range(0x41, 0x5A+1):
            a = "capital letter"
            print(f">>{input_value} is a {a} and its small-case letter is {input_value.lower()}")
        elif ord(input_value) in range(0x61, 0x7A+1):
            a = "small-case letter"
            print(f">>{input_value} is a {a} and its capital letter is {input_value.upper()}")
        else:
            a = "Special Character"
            print(f">>{input_value} is a {a}")
    else:
        print("Nothing Happen")
        continue