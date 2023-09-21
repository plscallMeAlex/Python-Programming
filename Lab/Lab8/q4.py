fn = str(input("Enter your first name: "))
ln = str(input("Enter your last name: "))
gd = str(input("Enter your gender (m/f): "))

username = gd + ln[0] + fn[0:6]
print(f"Your username: {username.upper()}")