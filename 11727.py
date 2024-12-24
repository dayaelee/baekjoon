n = int(input())

dp = [0, 1, 3,]

for i in range(3, n+1):
    tmp = dp[i-1] + (dp[i-2]*2)
    dp.append(tmp%10007)

print(dp[n])
