def power(s):
    s_list = list(s)
    n = len(s_list)
    power_set = []
    for i in range(1 << n):
        subset = [s_list[j] for j in range(n) if (i & (1 << j)) > 0]
        power_set.append(set(subset))
    return power_set

s = {1, 2, 3}
result = power(s)
print(result)
