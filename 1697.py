from collections import deque
n, k = map(int, input().split())

visited=[False for _ in range(100001)]

def bfs(start, cnt):
    q=deque([[start, cnt]])
    visited[start]=True
    cnt = 0
    while q:
        now, cnt = q.popleft()
        if now == k:
            print(cnt)
            break

        if now+1<=100000:
            if visited[now+1]==False:
                visited[now+1]=True
                q.append([now+1, cnt+1])
        
        if now-1>=0:
            if visited[now-1]==False:
                visited[now-1]=True
                q.append([now-1, cnt+1])

        if now*2<=100000:
            if visited[now*2]==False:
                visited[now*2]=True
                q.append([now*2, cnt+1])
bfs(n, 0)
