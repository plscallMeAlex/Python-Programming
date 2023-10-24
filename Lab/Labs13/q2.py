def list_reversee(ls):
    return rev(ls,0,len(ls)-1)
def rev(ls, l, r):
    if l == r:
        return ls
    elif len(ls) % 2 == 0 and l - 1 == r:
        return ls
    else:
        ls[l],ls[r] = ls[r],ls[l]
        return rev(ls,l+1, r-1)

print(list_reversee([1,2,3,4,5,6,7,8]))