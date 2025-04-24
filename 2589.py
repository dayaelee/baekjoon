import sys
from collections import deque
import copy
input = sys.stdin.readline

dy=[-1, 1, 0, 0]
dx=[0, 0, -1, 1]

n, m = map(int, input().split())
mapp=[]
for i in range(n):
    mapp.append(list(input()))

originvisited=[[False] * m for _ in range(n)]

global reault
result=0

lSet=[]
def bfs(sy, sx):
    visited=copy.deepcopy(originvisited) # 방문여부 초기화 
    visited[sy][sx]=True
    q=deque([(sy, sx, 0)])

    check=0
    rem=[-1, -1]

    while q: # 지금으로부터 가장 멀때, 거리 얼마인지 찾기 bfs
        y, x, cnt = q.popleft()

        if cnt>check: # 클때만 갱신, 다 방문하면 알아서 소멸
            check=cnt
            rem[0], rem[1] = y, x

        for k in range(4):
            ny=y+dy[k]
            nx=x+dx[k]

            if 0<=ny<n and 0<=nx<m and visited[ny][nx]==False and mapp[ny][nx]=='L':
                visited[ny][nx]=True
                q.append((ny, nx, cnt+1))

    global result
    result=max(result, check)

visited=copy.deepcopy(originvisited)

lSet=[]
for i in range(n):
    for j in range(m):
        if mapp[i][j]=='L':
            lSet.append([i, j])

if len(lSet)==(n*m): # 모두 L인 경우, 중복된 짓을 여러번함. 그래서 한번만 시키기.
    y, x = lSet[i][0],lSet[i][1] 
    visited=bfs(y, x)
else:
    for i in range(len(lSet)):
        y, x = lSet[i][0],lSet[i][1] 
        bfs(y, x)

print(result)