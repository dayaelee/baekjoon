import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n = map(int, input().split()) # 세로, 가로 

dy=[-1, 1, 0, 0]
dx=[0, 0, -1, 1]

mapp=[]
for i in range(m):
    mapp.append(list(map(int, input().split())))

dp=[[-1] * n for _ in range(m)]

def dfs(y, x):
    if y==m-1 and x == n-1:
        dp[y][x]=1
        return dp[y][x]

    if dp[y][x]==-1: # 아무도 안갔음

        dp[y][x]=0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<m and 0<=nx<n and mapp[ny][nx] < mapp[y][x]:
                tmp = dfs(ny, nx)
                # print('ny, nx',ny, nx, " tmp: ",  tmp)
                if tmp:
                    dp[y][x]+= tmp
                    # print('y, x',y, x, " tmp: ",  tmp, 'dp[y][x]', dp[y][x])

            
    return dp[y][x]
                
dfs(0, 0)

print(dp[0][0])