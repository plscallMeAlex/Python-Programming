s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

def product(*i):
    if not i:
        return [()]
    res = [()]
    for current_set in i:
        temp_res = []
        for item in current_set:
            for prod in res:
                temp_res.append(prod + (item,))
        res = temp_res
    return res


print(product(s1,s2))
print()
print(product(s1,s2,s3))
print()
print(product(s1))