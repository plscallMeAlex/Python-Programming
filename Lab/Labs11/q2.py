import math

class Calculator:
    def __init__(self, acc=0.00):
        self.acc = acc
    def set_accumulator(self, a):
        self.acc = a
    def get_accumulator(self):
        return self.acc
    def add(self, x):
        self.acc += x
    def subtract(self, x):
        self.acc -= x
    def multiply(self, x):
        self.acc *= x
    def divide(self, x):
        if x == 0: return self.x
        else: self.acc /= x
    def print_result(self):
        print(f"Result: {self.acc}")
    
class Sci_calc(Calculator):
    def __init__(self, acc =0.00):
        super().__init__(acc)
    def square(self):
        self.acc = math.pow(self.acc, 2)
    def exp(self, x):
        self.acc = math.pow(self.acc, x)
    def factorial(self):
        for i in range(1,self.acc):
            self.acc *= i
    def print_result(self):
        print("Result: {:e}".format(self.acc))

cal = Sci_calc(50)
cal.square()
cal.print_result()

cal.multiply(10)
cal.print_result()