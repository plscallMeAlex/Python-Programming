dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p':'1', 'q':'2', 'r':'3'}

def composite(l1, l2):
    newdict = {}
    for i in l1:
        if l1.get(i) in l2:
            newdict[i] = l2.get(l1.get(i))

    return newdict


a = composite(dict1, dict2)
print(a)