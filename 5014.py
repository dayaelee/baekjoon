from collections import deque
import heapq
f, s, g, u, d = map(int, input().split())

global cnt
cnt = 0
visited=[False] * (f+1)
def bfs(f, s, g, u, d, cnt):

    q=[(s, cnt)]
    
    check = 0
    while q:
        now, cnt = heapq.heappop(q)
        visited[now] = True
        if now == g:
            check = 1
            print(cnt)
            break

        if now + u<=f: # 올라가는 경우 
            if visited[now+u] == False:
                heapq.heappush(q, (now+u, cnt+1))
        
        if now - d>=1:
            if visited[now-d] == False:
                heapq.heappush(q,(now-d, cnt+1))
    if check == 0:
        print("use the stairs")

bfs(f,s,g,u,d,cnt)