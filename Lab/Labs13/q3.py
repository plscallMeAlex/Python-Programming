def gcd(x,y):
    if x == x and y == 0:
        return x
    else:
        return gcd(y, x % y)
    
print(gcd(10,20))