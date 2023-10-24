from turtle import *
t = Turtle()

def cross(leng,n):
    if n <= 0:
        pass
    else:
        for i in range(4): #for looping in each arm
            t.fd(leng)
            if n == 1:
                t.dot()
            cross(leng/2, n-1)
            t.backward(leng)
            t.right(90)


cross(100,1)
done()