import sys
from collections import deque
from collections import defaultdict
n, m = map(int, input().split())

d=[1, 2, 3 ,4, 5,6]

visited=[False] *101
l = defaultdict(int)
s = defaultdict(int)

for i in range(n):
    x, y = map(int, input().split())
    # ladder.append((x, y))
    l[x]=y

for i in range(m):
    u, v = map(int, input().split())
    # snake.append((u, v))
    s[u]=v

q=deque([(0, 1)])

while q:
    cnt, i = q.popleft()

    if i == 100:
        print(cnt)
        break

    for j in range(6):
        ni = i + d[j]

        if 1<ni<=100 and visited[ni]==False:
            if ni in l:
                visited[ni]=True
                if l[ni]<=100 and visited[l[ni]]==False:
                    visited[l[ni]]=True
                    q.append((cnt+1, l[ni]))
            elif ni in s:
                visited[ni]=True
                if visited[s[ni]]==False:
                    visited[s[ni]]=True
                    q.append((cnt+1, s[ni]))
            else:
                visited[ni]=True
                q.append((cnt+1, ni))
            

