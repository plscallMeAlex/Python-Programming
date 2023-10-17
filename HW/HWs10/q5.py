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