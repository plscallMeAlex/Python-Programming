# short = str(input("Short: "))
# long = str(input("Long: "))
# co = 0
# for i in short:
#     for k in long: 
#         if k == i:
#             co += 1
#             continue
#         else:
#             continue 
# if co > 0:
#     print("IS")
# else:
#     print("not")

short = input("Short: ")
long = input("Long: ")
co = 0

for i in range(len(long) - len(short) + 1):
    found = True
    for j in range(len(short)):
        if long[i + j] != short[j]:
            found = False
            break
    if found:
        co += 1

if co > 0:
    print("IS")
else:
    print("not")
