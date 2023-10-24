def perm(t):
    newt = list(t)
    if len(t) == 1:
        return [newt]
    else:
        r = []
        for i in range(len(newt)):
            su = newt[0:i] + newt[i+1:]
            tuplex = perm(su)
            for j in tuplex:
                r.append(newt[i:i+1] + j)
        return r

def permprint(t,n):
    a = perm(t)
    for i in a:
        print(tuple(i[0:n]))

permprint((1, 2, 3, 4), 3)

