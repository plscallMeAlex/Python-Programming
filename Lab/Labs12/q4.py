sup = set([1, 2, 3, 4])
sub = set([1, 2, 4])

def my_subset(o,s):
    for i in o:
        if i in s:
            continue
        else:
            return False
    return True


print(my_subset(sub, sup))
print(my_subset(sup, sub))
