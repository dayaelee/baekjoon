import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m, r = map(int, input().split())

graph=[[] for _ in range(n+1)]

for i in range(m):
    u, v= map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

v = [i for i in range(1, n+1)]
for node in range(n+1):
    if graph[node]:
        graph[node].sort(reverse=True)


global cnt
cnt=0
visited=[False] * (n+1)
result=[0]*(n+1)
def dfs(v, e, r):
    global cnt
    cnt+=1
    result[r]= cnt
    visited[r]=True
    check =0
    for node in e[r]:
        if visited[node] == False:
            check=1
            dfs(v, e, node)
    
dfs(v, graph, r)

for i in range(1, len(result)):
    print(result[i])
