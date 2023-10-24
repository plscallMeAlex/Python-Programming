def f(n):
    if n == 0:
        print(0)
        return 0
    if n > 0 and n % 2 == 0:
        a = 2 * f(n/2) + 1
        print(a)
        return a
    else:
        print(0)
        return 0
    print(n)

f(4)