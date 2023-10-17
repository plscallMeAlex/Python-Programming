def get_the_difference(f,s):
    nlist = []
    for i in f:
        if i in s:
            continue
        else:
            nlist.append(i)
    for i in s:
        if i in f:
            continue
        else:
            nlist.append(i)
    print(nlist)

get_the_difference([3,1,1,1,2,7], [4,1,1,2,2,5])