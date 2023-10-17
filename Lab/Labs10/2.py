def remove_the_thirds(d):
    x = 0
    for i in range(0,len(d)):
        if (i+1) % 3 == 0:
            d.pop(i - x)
            x += 1
        

list1 = [3,6,6,3,7,2,0,1,5,4]
print(list1)
remove_the_thirds(list1)
print(list1)