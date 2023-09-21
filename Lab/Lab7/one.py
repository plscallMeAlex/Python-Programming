class Time():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def printit(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} Hrs.")
    
time1 = Time(9, 30, 0)
time1.printit()