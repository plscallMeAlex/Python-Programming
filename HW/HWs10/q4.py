def print_table(n:[[]]):
    for i in n:
        for j in i:
            print(j, end='\t')
        print()
            
a = [["x", "y"], [0, 0], [10, 10], [200, 200]]
print_table(a)
print()
print_table([
    ["ID", "Name", "Surname"],
    ["001", "Guido", "van Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"]
])