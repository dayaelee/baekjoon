import sys
input=sys.stdin.readline
n, m = map(int, input().split())
from collections import deque

if n==0 and m==0:
    print(0)
    print(0)
    exit(0)

dy=[1, -1, 0, 0]
dx=[0, 0, 1, -1]

tmp=[]
for i in range(n):
    tmp2=list(map(int, input().split()))
    tmp.append(tmp2)

# 그냥 카운트만 하는애 cnt
# 방문 확인용 visited
cnt = 0
visited = [([False] * m) for _ in range(n)]
bigN = 0
def bfs(cnt, dequeA, visited):
    bigN=1
    while dequeA:
        yy, xx, _ = dequeA.popleft()
        visited[yy][xx] = True
        for i in range(4): 
            nx=xx+dx[i]
            ny=yy+dy[i]

            if ny<0 or nx<0 or ny>=n or nx>=m:
                continue
            if visited[ny][nx]==True:
                continue
            if tmp[ny][nx]==0:
                continue

            if tmp[ny][nx]>=1 and visited[ny][nx]==False:
                tmp[ny][nx] = bigN+1
                bigN=bigN+1
                visited[ny][nx]=True
                dequeA.append([ny,nx, bigN])
    return cnt, bigN

tmp3=[]
check = 0
dequeA = deque()
for i in range(n):
    for j in range(m):
        if tmp[i][j] == 1 and visited[i][j] == False:
            dequeA.append([i,j, 1])
            cnt+=1
            cnt, bigN = bfs(cnt, dequeA, visited)
            tmp3.append(bigN)
            check =1
print(cnt)
if n == 0 and m ==0 or check ==0:
    print(0)
else:
    print(max(tmp3))

