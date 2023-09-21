class Poly():
    def __init__(self, a):
        self.a = a
    
    def add(self, p):
        lismax = max(len(self.a), len(p.a))
        samea = self.a
        for i in range(lismax):
            if i>= len(self.a) or self.a[i] is None:
                self.a += (0,)
            if i >= len(p.a) or p.a[i] is None:
                p += (0,)
        result = ()
        for i in range(lismax):
            resultsum = self.a[i] + p.a[i]
            result += (resultsum,)
        self.a = samea
        return Poly(result)
    
    def scalar_multiply(self,n):
        samea = self.a
        result = ()
        for i in range(len(self.a)):
            result += (self.a[i] * n,)
        self.a = samea
        return result
    
    def multiply(self, p):
        samea = self.a
        result = [0] * (len(self.a) + len(p) -1)
        for i in range(len(self.a)):
            for k in range(len(p)):
                b = (self.a[i] * p[k])
                result[i+k] += b
        result = tuple(result)
        self.a = samea
        return result
    
    def power(self, n):
        result = self
        for i in range(n-1):
            result = result.multiply(self.a)
        return Poly(result)

    def diff(self):
        samea = self.a
        result = ()
        for i in range(len(self.a)):
            if self.a[i] * i == 0:
                continue
            result += (self.a[i] * i,)
        self.a = samea
        return Poly(result)
    
    def integrate(self):
        samea = self.a
        result = ()
        for i in range(len(self.a)+1):
            if i == 0:
                result += (0,)
                continue
            result += (self.a[i-1] / i,)
        self.a = samea
        return result
    
    def eval(self, n):
        samea = self.a
        result = 0
        for i in range(len(self.a)):
            result += self.a[i]*(n**i)
        self.a = samea 
        return result

    def print_out(self):
        for i in range(len(self.a)):
            if i == 0:
                print(f"{self.a[i]}", end='')
            else:
                if self.a[i] == 0:
                    continue
                if self.a[i] > 0:
                    if i == (len(self.a) - 1):
                        print(f" + {self.a[i]}" + f"x^{i}")
                    else:  
                        print(f" + {self.a[i]}" + f"x^{i}", end='')
                else:
                    if i == (len(self.a) - 1):
                        print(f" - {abs(self.a[i])}" + f"x^{i}")
                    else:
                        print(f" - {abs(self.a[i])}" + f"x^{i}", end='')
                    

    

p = Poly((1,0,-2))
p.print_out()

q = p.power(2)
q.print_out()

p.eval(3)

r = p.add(q)
r.print_out()

r.diff().print_out()
