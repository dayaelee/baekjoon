n, k = map(int, input().split())

dp=[[0]* (n+1) for _ in range(k)]

for i in range(k):
    for j in range(n+1):
        if i == 0:
            dp[i][j]=1
        else:
            if j == 0:
                dp[i][j]=1
            else:
                dp[i][j]= dp[i-1][j]+ dp[i][j-1]

print(dp[-1][-1])

