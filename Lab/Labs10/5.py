# list1 = int(input("Enter list1: ")).split()
# list2 = int(input("Enter list2: ")).split()

list1 = [1, 5, 16, 61, 111]
list2 = [2, 4, 5, 6]

# def merge(list1, list2):
#     result = list1 + list2
#     # for i in range(0,len(result)):
#     #     if i == len(result) -1:
#     #         break
#     #     elif result[i] > result[i+1]:
#     #         result[i] = result[i+1:i+2]
#     #         result[i+1] = result[i:i+1]
#     #     else:
#     #         continue
#     # for i in range(0,len(result)):
#     #     for j in range(0,len(result)):    
#     #         if i == len(result)-1:
#     #             break
#     #         elif result[i] > result[i+1]:
#     #             result[i]result[i+1]
#     #             result[i+1] = result[i]
#     #         else:continue
#     # for i in range(0, len(result)):
#     #     for j in result:
#     #         if
def merge(list1, list2):
    # Merge the two lists
    merged_list = list1 + list2
    
    # Bubble sort to sort the merged list in ascending order
    n = len(merged_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

    print(f"The merged list is {merged_list}")

merge(list1, list2)
