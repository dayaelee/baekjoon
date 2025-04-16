import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

dy=[0, 1, 1] #우, 좌하, 하
dx=[1, 1, 0]

mapp=[[0]*(n+1)]
for i in range(n):
    mapp.append([0]+list(map(int, input().split())))

dp = [[[0]*3 for _ in range(n+1)] for _ in range(n+1)]
dp[1][2][0]=1

for i in range(1, n+1):
    for j in range(1, n+1):
        if mapp[i][j] == 1:
            continue

        if j-1>=1:
            dp[i][j][0] += dp[i][j-1][2]+ dp[i][j-1][0]
        
        if i-1>=1:
            dp[i][j][1] += dp[i-1][j][1]+dp[i-1][j][2]
        
        if i-1>=1 and j-1>=1:
            if mapp[i-1][j]==0 and mapp[i][j-1]==0:
                dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1]+ dp[i-1][j-1][2]

print(dp[n][n][0]+dp[n][n][1]+dp[n][n][2])               
        