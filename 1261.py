import sys
from collections import deque
input = sys.stdin.readline

dy=[1, -1, 0, 0]
dx=[0, 0, 1, -1]

m, n = map(int, input().split())
mapp = []
for i in range(n):
    mapp.append(list(input().strip()))

visited=[[False for _ in range(m+1)] for _ in range(n+1)]

def bfs(starty, startx):
    q = deque([(starty, startx, 0)])
    visited[starty][startx] = True

    while q:
        y, x, cnt = q.popleft()
        
        if y==n-1 and x==m-1:
            
            print(cnt)
            return
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
    
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx]==False:
                    visited[ny][nx]=True
                    if mapp[ny][nx]=='1':
                        q.append((ny, nx, cnt+1))
                    else:
                        q.appendleft((ny, nx, cnt))

bfs(0, 0)

#벽을 부수지 않는 칸을 이용해서 우선순위를 매겨서 큐에 넣음



        


