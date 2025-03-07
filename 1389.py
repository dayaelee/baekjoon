import sys
input = sys.stdin.readline


n, m = map(int, input().split())

dp=[[float("inf")] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if j == 0:
            dp[i][j]=0
        if i == j:
            dp[i][j]=0

for i in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

minValue = float("inf")
check = -1
for index, i in enumerate(dp):
    dp[index]=sum(i)
    if minValue>dp[index]:
        check = index
        minValue=dp[index]
print(check)
