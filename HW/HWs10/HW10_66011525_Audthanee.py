#Q1
from matplotlib.pyplot import pie, show

def pie_chart(inp):
    new = []
    count = []
    for i in inp:
        if i not in new:
            new.append(i)
    for i in new:
        a = inp.count(i)
        count.append(a )
    pie(count, labels=new)
    show()
    
pie_chart([3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3])
#-----------------------------------------------------------------------------------------------------------
#Q2
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
#-----------------------------------------------------------------------------------------------------------
#Q3
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
#-----------------------------------------------------------------------------------------------------------
#Q4
def print_table(n:[[]]):
    for i in n:
        for j in i:
            print(j, end='\t')
        print()
            
a = [["x", "y"], [0, 0], [10, 10], [200, 200]]
print_table(a)
print()
print_table([
    ["ID", "Name", "Surname"],
    ["001", "Guido", "van Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"]
])
#-----------------------------------------------------------------------------------------------------------
#Q5
def isAnagram(st1, st2):
    l1 = list(st1)
    l2 = list(st2)
    if len(st1) != len(st2):
        return False
    else:
        count = 0
        for i in l1:
            for j in l2:
                if j == i:
                    count += 1
                    l2.remove(j)
                    break

        if count == len(l1):
            return True
        else:
            return False

print(isAnagram("silent","listen"))
print(isAnagram("heart", "earth"))
print(isAnagram("cinema", "iceman"))
print(isAnagram("jelly", "jam"))
print(isAnagram("pizza", "zipline"))
#-----------------------------------------------------------------------------------------------------------