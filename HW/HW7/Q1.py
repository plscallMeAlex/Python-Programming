class Clock():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def settime(self, inhour, inmin, insec):
        self.hour = inhour
        self.minute = inmin
        self.second = insec
    def get_time(self):
        if self.hour == 24:
            nhour = self.hour-12
            display = "AM."
        elif self.hour > 12:
            nhour = self.hour - 12
            display = "PM."
        elif self.hour == 0:
            nhour = self.hour + 12
            display = "AM."
        elif self.hour == 12:
            nhour = self.hour
            display = "PM."
        else:
            nhour = self.hour
            display = "AM."
        print(f"{nhour:02d}:{self.minute:02d}:{self.second:02d} {display}")
    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.second -= 60
            self.minute += 1
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        if self.hour > 24: 
            self.hour -= 24


a = Clock(14, 30, 59)
a.get_time()

a.tick()
a.get_time()

a.settime(1, 40, 50)
a.get_time()
