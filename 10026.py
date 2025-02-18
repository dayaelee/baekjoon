import sys
from collections import deque
input = sys.stdin.readline
# 적록색약은 G-R를 구분하지 못함.
dy=[1, -1, 0, 0]
dx=[0, 0, -1, 1]

n = int(input())

mapp=[]
for i in range(n):
    mapp.append((list(input().strip())))
visited=[[False] * n for _ in range(n)]

def dfs(y, x):
    q=deque([(y, x, mapp[y][x])])
    visited[y][x]=True
    check = 0
    while q:
        y, x, value = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<n and visited[ny][nx]== False:
                    if mapp[ny][nx]==value:
                        check +=1
                        visited[ny][nx]=True
                        q.append([ny, nx, mapp[ny][nx]])
    return check

def dfs2(y, x):
    q=deque([(y, x, mapp[y][x])])
    visited2[y][x]=True
    check = 0
    while q:
        y, x, value = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<n and visited2[ny][nx]== False:
                    if value == "G" or value == "R":
                        if mapp[ny][nx]=="G" or mapp[ny][nx]== "R":
                            check +=1
                            visited2[ny][nx]=True
                            q.append([ny, nx, mapp[ny][nx]])
                    else:
                        if value == mapp[ny][nx]:
                            check +=1
                            visited2[ny][nx]=True
                            q.append([ny, nx, mapp[ny][nx]])
    return check



global cnt 
cnt=0

for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            check = dfs(i, j)
            cnt+=1

visited2=[[False] * n for _ in range(n)] 

global cnt2 
cnt2=0

for i in range(n):
    for j in range(n):
        if visited2[i][j]==False:
            check = dfs2(i, j)
            cnt2+=1

print(cnt, cnt2)