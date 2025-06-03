import sys
from collections import deque
input = sys.stdin.readline 

n, m, r = map(int, input().split())
graph=[[] for _ in range(n+1)]
nodes=[i for i in range(1, n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

visited=[False] * (n+1)
result = [0] * (n+1)
global cnt 
cnt=1
def bfs (v, e, r):
    global cnt
    visited[r]=True
    q=deque([(r)])
    while q:
        node = q.popleft()
        result[node]=cnt
        cnt+=1
        for no in e[node]:
            if visited[no]==False:
                visited[no]=True
                q.append((no))
    
bfs(nodes, graph, r)
for i in result[1:]:
    print(i)