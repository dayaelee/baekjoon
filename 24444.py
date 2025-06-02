import sys
from collections import deque
input = sys.stdin.readline
n, m, r = map(int, input().split())

graph=[[] for _ in range(0, (n+1))]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

nodes=[i for i in range(n+1)]

for i in range(n+1):
    graph[i].sort()

result=[0] * (n+1)
def bfs(v, e, r):
    visited=[False]*(n+1)
    visited[r]=True
    q=deque([r])
    cnt = 1
    while q:
        u = q.popleft()
        result[u]=cnt
        cnt+=1
        for node in graph[u]:
            if visited[node]==False:
                visited[node]=True
                q.append(node)

bfs(nodes, graph, r)
for i in result[1:]:
    print(i)



