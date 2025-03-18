s = list(input())
dp=[0] * 26
for i in s:
    indexx=ord(i)-97
    dp[indexx]+=1
print(' '.join(map(str, dp)))


