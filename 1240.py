import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph={}
costs=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1):
    a, b, cost = map(int, input().split())
    costs[a][b] = cost
    costs[b][a] = cost
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

for t in range(m):
    a, b = map(int, input().split())
    
    visited=[False for _ in range(n+1)]
    def dfs(start, end, cost):
        if start == end:
            print(cost)
            return

        for node in graph[start]:
            if visited[node] == False:
                visited[node]=True
                dfs(node, end, cost+ costs[start][node])
                visited[node]=False
    visited[a]=True
    dfs(a, b, 0)
        