# 91에서 컷 
import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


mapp=[]
n, m = map(int, input().split())
for i in range(n):
    mapp.append(list(input().strip()))

dp=[[-1 for _ in range(m)] for _ in range(n)] # 기본 -1
# 못가면 0

# print(mapp)
cnt = 0

def dfs(y, x):
    global cnt
    if mapp[y][x] =='U':
        ny = y+ dy[0]
        nx = x+ dx[0]
    elif mapp[y][x]=='R':
        ny = y+ dy[1]
        nx = x+ dx[1]
    elif mapp[y][x]=='D':
        ny = y+ dy[2]
        nx = x+ dx[2]
    elif mapp[y][x]=='L':
        ny = y+ dy[3]
        nx = x+ dx[3]
        
    if 0>ny or ny>=n or 0>nx or nx>=m:
        dp[y][x]=0
        return 0
    if dp[ny][nx] ==-1:
        dp[ny][nx]= 1
        result = dfs(ny, nx)
        if result == 0:
            dp[ny][nx]= 0
            dp[y][x]
            cnt+=1
            return 0
        else:
            dp[ny][nx]= 1
            dp[y][x]
            return 1
    elif dp[ny][nx] == 0:
        return 0
    
for i in range(n):
    for j in range(m):
        if dp[i][j]== -1 :
            result = dfs(i, j)
            if result == 0:
                dp[i][j]= 0
                cnt+=1
            else:
                dp[i][j]= 1
# print(dp)
print(cnt)