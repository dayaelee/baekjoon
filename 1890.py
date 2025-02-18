import sys
from collections import deque
input = sys.stdin.readline

mapp=[]
n = int(input())
for i in range(n):
    mapp.append(list(map(int, input().split())))

dp=[[0] * n for _ in range(n)]
dp[0][0]=1

for i in range(n):
    for j in range(n):
        if dp[i][j]>0 and mapp[i][j]>0:
            #우측
            if j+mapp[i][j]<n:
                dp[i][j+mapp[i][j]]+=dp[i][j]
            #아래측
            if i+mapp[i][j]<n:
                dp[i+mapp[i][j]][j]+=dp[i][j]

print(dp[n-1][n-1])