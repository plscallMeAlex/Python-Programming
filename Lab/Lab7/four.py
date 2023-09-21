from math import sqrt
class QuardraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getDiscriminant(self):
        discriminant = self.__b**2 - 4*(self.__a*self.__c)
        return discriminant
    def getRoot1(self):
        discre = self.getDiscriminant()
        if self.__b**2 - 4*(self.__a*self.__c) >= 0:    
            root1 = (-self.__b + sqrt(discre))/(2*self.__a)
            return root1
        else:
            return None
    def getRoot2(self):
        discre = self.getDiscriminant()
        if self.__b**2 - 4*(self.__a*self.__c) >= 0:
            root2 = (-self.__b - sqrt(discre))/(2*self.__a)
            return root2
        else:
            return None
        
a = QuardraticEquation(3,5,7)
print(a.getRoot1())
print(a.getA())
print(a.getB())
print(a.getC())
print(a.getDiscriminant())