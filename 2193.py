n = int(input())

dp=[[0, 0], [0, 1]]
for i in range(2, n+1):
    tmp = []
    tmp.append(dp[i-1][0] + dp[i-1][1])
    tmp.append(dp[i-1][0])
    dp.append(tmp)


print(dp[n][0] + dp[n][1])


