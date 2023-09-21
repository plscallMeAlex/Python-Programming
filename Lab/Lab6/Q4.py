def sum_of_digits(inte):
    new = []
    for x in str(inte):
        new.append(int(x))
    result = sum(new)
    return result

sum_of_digits(234)
print(sum_of_digits(234))