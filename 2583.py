from collections import deque
m, n, k = map(int, input().split())

mapp=[[0]*n for _ in range(m)]

dy=[1, -1, 0, 0]
dx=[0, 0, -1, 1]

start = []
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for ii in range(y1, y1+(y2-y1)):
        for j in range(x1, x1+(x2-x1)):
            mapp[ii][j]=1

global cnt
cnt = 0
answer = []
def bfs(starty, startx):
    q = deque([(starty, startx, 1)])
    cnt = 0
    while q:
        y, x, length = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<m and 0<=nx<n and mapp[ny][nx]==0:
                mapp[ny][nx]=1
                cnt +=1
                q.append((ny, nx, length+1))
    if cnt ==0:
        cnt +=1
    return cnt 

for i in range(m):
    for j in range(n):
        if mapp[i][j]==0:
            answer.append((bfs(i, j)))
            cnt +=1
print(cnt)
print(' '.join(map(str,sorted(answer))))