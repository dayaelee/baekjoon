import sys
input = sys.stdin.readline

n, k = map(int, input().split())
basket = []
for i in range(n): # w, v
    basket.append(list(map(int, input().split())))
dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight, value = basket[i-1]
        if weight>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j] = max(value+dp[i-1][j-weight], dp[i-1][j])

print(dp[-1][-1])
