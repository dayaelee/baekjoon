import sys
from collections import deque
input = sys.stdin.readline

dy=[1, -1, 0, 0]
dx=[0, 0, -1, 1]
mapp=[]
n, m = map(int, input().split())

for i in range(n):
    tmp = list(input())
    mapp.append(tmp)
    for j in range(m):
        if tmp[j]=='I':
            yy, yx = i, j
visited=[[False]*m for _ in range(n)]
q=deque([(yy, yx)])
visited[yy][yx]=True
global answer
answer = 0

while q:
    print('q', q)
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0<=ny<n and 0<=nx<m and visited[ny][nx]==False) and (mapp[ny][nx]=='O' or mapp[ny][nx]=='P'):
            visited[ny][nx]=True
            if mapp[ny][nx]=='O':
                q.append((ny, nx))
            elif mapp[ny][nx]=='P':
                answer+=1
                q.appendleft((ny, nx))

if answer>=1:
    print(answer)
else:
    print('TT')






