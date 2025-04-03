from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dy=[1, -1, 0, 0]
dx=[0, 0, -1, 1]
mapp=[]
ty, tx= 0, 0

visited=[[False] * m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j]==2:
            ty, tx = i, j
    mapp.append(tmp)

def bfs(ty, tx):
    q=deque([(ty, tx)])
    mapp[ty][tx]= 0
    visited[ty][tx] = True
    while q:
        
        y, x = q.popleft()
        
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=ny<n and 0<=nx<m and mapp[ny][nx]!=0 and visited[ny][nx]==False:
                if mapp[ny][nx]<=mapp[y][x]+1:
                    visited[ny][nx]=True
                    mapp[ny][nx]=mapp[y][x]+1
                    q.append((ny,nx))

bfs(ty, tx)

for i in range(n):
    for j in range(m):
        if mapp[i][j]==1 and visited[i][j]==False:
            mapp[i][j]=-1


for i in mapp:
    print(' '.join(map(str, i)))