def sorting(inp:[]):
    for j in range(0,len(inp)-1):
        for i in range(0,len(inp)-1):
            if inp[i] > inp[i+1]:
                inp[i], inp[i+1] = inp[i+1], inp[i]
            else:
                continue
    return inp
        
inp = [3, 2 ,9, 7, 8]
print(f"Input: {inp}")
print(f"Output: {sorting(inp)}")