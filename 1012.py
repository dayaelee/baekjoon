import sys
from collections import deque
input=sys.stdin.readline

dx= [0, 0, 1, -1]
dy= [1, -1, 0, 0]

answer=[]
def bfs(y, x):
        queue = deque()
        visited[y][x] = True
        queue.append([y, x])

        while queue:
            ny, nx = queue.popleft()
            for ii in range(4):
                yy= ny+dy[ii]
                xx= nx+dx[ii]

                if 0<=yy<n and 0<=xx<m and mapp[yy][xx]==1 and  visited[yy][xx] == False:
                    visited[yy][xx] = True
                    queue.append([yy, xx])

t = int(input())
for j in range(t):
    m, n, k = map(int, input().split())
    mapp = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(k):
        wm, wn = map(int, input().split())
        mapp[wn][wm] = 1
    
    for ix in range(n):
        for jx in range(m):
            if mapp[ix][jx]==1 and visited[ix][jx] == False:
                    cnt+=1
                    bfs(ix, jx)
    answer.append(cnt)

for i in answer:
  print(i)