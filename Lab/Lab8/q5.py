def LCS(s1,s2):
    x = 0
    result = str()
    for i in range(len(s1)):
        for j in range(i+1, len(s1)+ 1):
            if s1[i:j] in s2:
                if len(s1[i:j]) > x:
                    result = s1[i:j]
                    x = len(s1[i:j])
                # else:
                #     result 

    print(result)
LCS("ingenious", "intelligent")
LCS("intelligent", "inconsidered")
LCS("russian", "ukrainian")
LCS("","")





        # for j in range(len(s2)):
        #     if s2[j] == s1[i]:
        #         i += 1
        #         result += s2[j]
        #         pass
        #     else:
        #         continue
        #     if x < len(result):
        #         x = len(result)
        #     else:
        #         break
            
        # if x < len(result):
        #     x = len(result)







# def LCS(s1, s2):
#     m, n = len(s1), len(s2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#     max_len = 0  # To keep track of the length of the LCS
#     end_index = 0  # To keep track of the ending index of the LCS in s1

#     # Build the DP table and track the length and ending index of LCS
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#                 if dp[i][j] > max_len:
#                     max_len = dp[i][j]
#                     end_index = i

#     # Reconstruct the LCS from the ending index
#     if max_len == 0:
#         return ""  # No common substring found
#     else:
#         start_index = end_index - max_len
#         return s1[start_index:end_index]

# result = LCS("ingenious", "intelligent")
# print(result)
