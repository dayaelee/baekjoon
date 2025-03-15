# import sys
# input = sys.stdin.readline


# n = int(input())
# dp = [-9] * 11
# check = [0] * 11
# for i in range(n):
#     cn, w = map(int, input().split())
#     if dp[cn]== -9:
#         dp[cn] = w
#         check[cn]+=1
#     else:
#         if dp[cn]!=w:
#             check[cn]+=1
# print(check)

# # answer = 0
# # for i in dp:
# #     if i ==0:
# #         continue
# #     else:
# #         answer= max(answer, i)
# # print(answer-1)

# print(max(check))

n = int(input())
 
arr = {}
count = 0
 
for i in range(n):
    a,b = map(int, input().split())
    if a not in arr:
        arr[a] = b
    else:
        if arr[a] != b:
            count +=1
            arr[a] = b
 
print(count)