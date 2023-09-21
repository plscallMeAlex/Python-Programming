while True:
    n = int(input("Input interger: "))
    if n >= 1 :#make user must input number that greater than 0
        break
    else:
        print("Input number that greater than 0")
        continue

print()
print()
for line in range(n,0,-1):
    all_line = (2*line) -1
    for eline in range(0,all_line+1):
        if eline == 0 and (n< line < 0):#condition that will overlapping the star at the 2nd wave and the wave before the last wave
            continue
        if eline < line : #step_up
            for k in range(0,eline+1):
                print("*", end="")
            print()    
        elif eline == all_line:
            continue
        else: #step down
            for k in range(eline,all_line):
                print("*", end="")
            print()
