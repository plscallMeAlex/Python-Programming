x = input("Please enter a character: ")
o = ord(x)
z = format(o, '04x')
print("The Unicode of \"{}\" is u{}.".format(x, z))
