line = int(input("Enter the number of lines: "))

if line % 2 == 0:
    for x in range(1, (line - (line // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((line - (line // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

if line % 2 != 0:
    for x in range(1,(line - ((line+1) // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((line - ((line-1) // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()