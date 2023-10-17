def name_list():
    count = 0
    a = []
    while True:
        count += 1
        inp = input(f"Enter name {count}: ")
        if inp == "" or inp == " ":
            print(a)
            break
        else:
            a.append(inp)
name_list() 