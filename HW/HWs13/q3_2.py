def perm3(t):
    newt = list(t)
    if len(t) == 1:
        return [newt]
    else:
        r = []
        for i in range(len(newt)):
            su = newt[0:i] + newt[i+1:]
            tuplex = perm3(su)
            for j in tuplex:
                r.append(newt[i:i+1] + j)
        return r

def permprint(t):
    a = perm3(t)
    for i in a:
        print(tuple(i[0:3]))

permprint((1, 2, 3))

