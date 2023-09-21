from tkinter import *
from tkinter import messagebox
class Converter:
    def __init__(self):
        window = Tk()
        window.geometry("150x150")
        window.title("Currency Converter")
        self.e1 = Entry(window, justify=RIGHT)
        self.e1.grid(row= 0)
        
        self.but1 = Button(window, text="USD -> THB", command=self.usbthb)
        self.but2 = Button(window, text="THB -> USD", command=self.thbusb)
        self.but1.grid(row= 1)
        self.but2.grid(row= 2)

        window.mainloop()

    def usbthb(self):
        try:
            inp = float(self.e1.get())
            money = inp * 30
            messagebox.showinfo("USD -> THB", f"{inp:.2f} USD = {money:.2f} THB")
        except  ValueError:
            messagebox.showerror("USD -> THB", "Error value")
    def thbusb(self):
        try: 
            inp = float(self.e1.get())
            money = inp / 30
            messagebox.showinfo("THB -> USD", f"{inp:.2f} THB = {money:.2f} USD")
        except ValueError:
            messagebox.showerror("THB -> USD", "Error value")

Converter()