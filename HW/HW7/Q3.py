class LinearEquation():
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getD(self):
        return self.d
    def getE(self):
        return self.e
    def getF(self):
        return self.f
    def isSolvable(self):
        if (self.a*self.d) - (self.b*self.c) == 0:
            return False
        else:
            return True
    def getX(self):
        if self.isSolvable() == True:   
            x = ((self.e*self.d) - (self.b * self.f)) / ((self.a * self.d) - (self.b * self.c))
            return x
        else:
            return "DNE"
    def getY(self):
        if self.isSolvable() == True:   
            y = ((self.a*self.f)-(self.e*self.c)) / ((self.a*self.d) - (self.b*self.c))
            return y
        else:
            return "DNE"

a = LinearEquation(1,2,3,4,5,6)
a.getA()
a.isSolvable()
a.getX()
a.getY()

print(a.getX())
print(a.getY())