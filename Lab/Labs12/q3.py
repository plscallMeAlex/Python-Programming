def inverse(dict):
    newdict = {}
    for k, v in dict.items():
        swp = []
        for i,j in dict.items():
            if j == v:
                if i not in swp:
                    swp.append(i)
                else:
                    swp.append(k)
                continue

                
        newdict[v] = set(swp)
    return newdict

dict = {'a':'1', 'b':'2', 'c':'1', 'd':'3', 'e':'1', 'f':'2'}
print(inverse(dict))