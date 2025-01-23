n = int(input())

dp=[1 for _ in range(1, 10)]
dp = [[0] +[0] + dp+[0]]

for i in range(n-1):
    dp.append([0 for j in range(0, 12)])


for i in range(1, n):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        
print(sum(dp[-1])%1000000000)