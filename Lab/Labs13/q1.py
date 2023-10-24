def member(num, listnum):
    if listnum[len(listnum)-1] == num:
        return True
    elif len(listnum) < 1:
        return False
    else:
        return member(num,listnum[0:len(listnum)-1])

x = member(2, [1,2,3])

print(x)