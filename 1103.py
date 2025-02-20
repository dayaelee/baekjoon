import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dy=[1, -1, 0, 0]
dx=[0, 0, -1, 1]
mapp=[]
n, m = map(int, input().split())
for i in range(n):
    mapp.append(list(input().strip()))
#print(mapp)

visited=[[False] * m for _ in range(n)]
dp=[[0] * m for _ in range(n)]

def backtrack(y, x, cnt):
    visited[y][x]=True
    global maxCnt
    maxCnt = max(cnt, maxCnt)
        
    for i in range(4):
        ny = y + (dy[i] * int(mapp[y][x]))
        nx = x + (dx[i] * int(mapp[y][x]))

        if 0<= ny < n and 0<= nx < m and mapp[ny][nx]!="H" and  cnt+1 > dp[ny][nx]:
            if visited[ny][nx]:
                print(-1)
                exit() 
                # 순환 구간이 하나라도 있으면 결국에 이 순환 구간 때문에 발목잡힘 = -1 출력하고 끝내는게 맞음 
            
            dp[ny][nx]=cnt+1
            visited[ny][nx]=True
            backtrack(ny, nx, cnt+1)
            visited[ny][nx]=False #갈때까지 가보고, maxCnt갱신만하고 다시 돌아와서 다시 탐색할 수 있음
    # 근데 for 문으로 움직여서 결국 끝나기 마련임. 
    # 끝은 난다. return 으로 인해서 
cnt = 0
maxCnt = 0
backtrack(0, 0, cnt)
print(maxCnt+1)