# def powerset(s):
#     x = len(s)
#     a = []
#     for i in range(1 << x):
#         a.append(s[j] for j in range(x) if (i & (1 << j)))
#     return a


# s = {1, 2, 3}
# n = powerset([-7, -3, -2, 5, 7])

# def summing(n):
#     if len(n) == 0:
#         return 
#     else:
#         if sum(n[0]) == 0:
#             print(n[0], end='')
#         summing(n[1:])

# summing(n)




def summingset(lst, index=0, current_subset=None, result=None):
    if current_subset is None:
        current_subset = []
    if result is None:
        result = []
    if index == len(lst):
        if sum(current_subset) == 0 and len(current_subset) != 0:
            result.append(current_subset.copy())
        return
    current_subset.append(lst[index])
    summingset(lst, index + 1, current_subset, result)
    current_subset.pop()
    summingset(lst, index + 1, current_subset, result)
    if index == 0:
        if len(result) <= 1:
            return "No"
        else:
            return f"Yes {result}"

lst1 = [-7, -3, -2, 5, 7]
lst2 = [2, -3, 5, 8, 11, 23, -1]
print(summingset(lst1))
print(summingset(lst2))