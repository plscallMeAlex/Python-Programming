from tkinter import *
import time

class Clock(object):
    def __init__(self, hh=0, mm=0, ss=0):
        self.h = hh
        self.m = mm
        self.s = ss
        self.running = True
    
    def run(self, label):
        if self.running:
            self.s += 1
            if self.s == 60:
                self.s = 0
                self.m += 1
            if self.m == 60: 
                self.m = 0
                self.h += 1
            if self.h == 24:
                self.h = 0
            time_str = "{:02d}:{:02d}:{:02d}".format(self.h, self.m, self.s)
            label.config(text=time_str)
        root.after(1000, self.run, label)  # Update the tkinter windo
    def stop(self):
        self.running = False
    
    def setTime(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

class AlarmClock(Clock):
    def __init__(self, hh=0, mm=0, ss=0):
        super().__init__(hh, mm, ss)
        self.alarm_hh = 0
        self.alarm_mm = 0
        self.alarm_ss = 0
        self.alarm_on_off = False
    
    def setAlarmTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s
    
    def alarm_on(self):
        self.alarm_on_off = True
    
    def alarm_off(self):
        self.alarm_on_off = False
    
    def run(self, label):
        super().run(label)
        if self.alarm_on_off and self.h == self.alarm_hh and self.m == self.alarm_mm and self.s == self.alarm_ss:
            label.config(text="Alarmmm!")
            self.stop()

# Create a tkinter window
root = Tk()
root.title("Clock and Alarm")

# Create a label to display the time
time_label = Label(root, font=("Helvetica", 48))
time_label.pack(pady=20)

# Initialize and run the AlarmClock
a = AlarmClock(0, 0, 0)
a.setAlarmTime(0, 0, 5)
a.alarm_on()
a.run(time_label)

# Start the tkinter main loop
root.mainloop()
