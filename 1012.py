import sys
input=sys.stdin.readline
from collections import deque

dx= [0, 0, 1, -1]
dy= [1, -1, 0, 0]

t = int(input())
for j in range(t):
    m, n, k = map(int, input().split())
    mapp = [[0] * m for _ in range(n)]
    for i in range(k):
        wm, wn = map(int, input().split())
        mapp[wn][wm] = 1

    visited = [[False] * m for _ in range(n)]

    list = deque()

    def bfs(y, x, visited):
        visited[y][x] = True
        list.append([y, x])

        while list:
            ny, nx = list.popleft()
            visited[ny][nx]= True
            for ii in range(4):
                yy= ny+dy[ii]
                xx= nx+dx[ii]

                if 0<=yy<n and 0<=xx<m and mapp[yy][xx]==1 and  visited[yy][xx] == False:
                    list.append([yy, xx])

    cnt = 0

    for ix in range(n):
        for jx in range(m):
            if mapp[ix][jx]==1:
                if visited[ix][jx] == False:
                    cnt+=1
                    bfs(ix, jx, visited)
    print(cnt)