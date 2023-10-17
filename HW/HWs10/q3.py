list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

def my_union(l1, l2):
    res = []
    for i in l1:
        res.append(i)
    for i in l2:
        if i in res:
            continue
        else:
            res.append(i)
    return res

def my_intersection(l1, l2):
    res = []
    for i in l1:
        if i in l2:
            res.append(i)
        else:
            continue
    return res

def my_difference(l1, l2):
    nlist = [x for x in l1 if x not in l2]
    return nlist

print(my_union(list1, list2))
print(my_intersection(list1, list2))
print(my_difference(list1, list2))