myDict = {'s5301': 'Fred', 's5302': 'Harry', 's5303': 'John', 's5304': 'Fred', 's5305': 'Harry'}

def find_duplicates(my_dict):
    newdict = {}
    for key, value in my_dict.items():
        for k, v in my_dict.items():
            if v == value and k!= key:
                newdict[key] = value
                break
    return newdict

duplicates = find_duplicates(myDict)
print(duplicates)
