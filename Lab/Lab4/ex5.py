cur_sum = 0
for i in range(5):
    ent = int(input("Enter an integer: "))
    if ent < 0 and cur_sum >= 0:
        cur_sum = 0
    
    cur_sum += ent
    print(f"Current sum: {cur_sum}")
