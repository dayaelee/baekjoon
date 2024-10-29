n = int(input())
tmp = list(map(int, input().split()))

dp = [1]*n
for i in range(len(tmp)):
    for j in range(0, i):
        if tmp[i]<tmp[j]:
            dp[i]= max(dp[i], dp[j]+1)

print(max(dp))