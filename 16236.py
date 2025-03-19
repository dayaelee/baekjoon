import sys
from collections import deque
n = int(input())
mapp = []

dy=[1, 0, 0, -1]
dx=[0, -1, 1, 0]
start = 2
babyY = -1
babyX = -1
for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        babyY=i
        babyX=tmp.index(9)
    mapp.append(tmp)

cnt = 0

global detailtime 
detailtime=0


def dfs(now, sy, sx, toy, tox, visited2, cnt):
    global detailtime
    if sy == toy and sx == tox:
        print('hi', cnt)
        detailtime = cnt
        return cnt

    for i in range(4):
        ny = sy+dy[i]
        nx = sx+dx[i]

        if 0<=ny<n and 0<=nx<n and visited2[ny][nx]==False:
            if mapp[ny][nx]<=now:
                visited2[ny][nx]=True
                cnt+=1
                dfs(now, ny, nx, toy, tox, visited2, cnt)

def bfs(start):
    global cnt
    global now
    now = start
    
    q=deque([(start, 0, babyY, babyX)])
    visited=[[False] * n for _ in range(n)] 
    visited[babyY][babyX]=True
    while 1:
        basket=deque([])
        print('!!', q, 'now', now)
        visited=[[False] * n for _ in range(n)] 
        while q:
            now, cnt, by, bx = q.popleft()
            
            for i in range(4):
                ny = by+dy[i]
                nx = bx+dx[i]

                if 0<=ny<n and 0<=nx<n and visited[ny][nx]==False:
                    if now > mapp[ny][nx]>0:
                        mapp[ny][nx]=0
                        cnt+=1
                        
                        visited[ny][nx]=True
                        q.append((now, cnt, ny, nx))
                        basket.append((now, cnt, ny, nx))
                        if now == len(basket):
                            now+=1
                            
                            print("??????? now", now)
                            cnt = 0
                            break
                    elif now == mapp[ny][nx] or mapp[ny][nx]==0:
                        visited[ny][nx]=True
                        q.append((now, cnt, ny, nx))
        print(basket,'basket, now', now)
        
        time = 0
        if basket:
            for i in range(len(basket)):
                visited2=[[False] * n for _ in range(n)] 
                if i == 0: 
                    sy, sx= babyY, babyX
                else:
                    sy, sx = basket[i-1][2], basket[i-1][3] 
                y, x = basket[i][2], basket[i][3]
                # print(sy, sx, y, x, visited2, 0)
                dfs(now, sy, sx, y, x, visited2, 0)
                time += detailtime
                print('time', time, 'detailtime', detailtime)
                q=deque([(now+1, 0, y, x)])
        else:
            break
        now+=1

print(bfs(2))         

