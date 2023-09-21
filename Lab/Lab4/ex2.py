a = input("Input any type of number:")
def main():
    if type(a) == float:
        b = str(input("floating(f) or scientific(s):"))
        if b in ["f", "floating", "F", "Floating"]:
            print(a)
        elif b in ["s", "S", "scientific", "Scientific"]:
            science = format(a, 'e')
            print(science)
    elif type(a) == int:
        c = str(input("binary, octal, hexadecimal, or decimal format: "))
        if c in ["binary", "b"]:
            binary = format(a, 'b')
            print(binary)
        elif c in ["octal", "o"]:
            octal = format(a, 'o')
            print(octal) 
        elif c in ["hexadecimal", "h"]:
            print(hex(a))
        elif c in ["decimal", "d"]:
            print(float(a))




if a.isdigit():
    a = int(a)
    main()
elif all(char.isdigit() or char in [".", "-"] for char in a):
    a = float(a)
    main()
elif isinstance(a, str):
    print("Nothing happen")

