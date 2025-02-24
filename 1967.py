import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

graph ={}

for i in range(n-1):
    a, b, cost = map(int, input().split())
    if a not in graph:
        graph[a] = [[b, cost]]
    else:
        graph[a].append([b, cost])
    if b not in graph:
        graph[b] = [[a, cost]]
    else:
        graph[b].append([a, cost])

visited=[-1 for _ in range(n+1)]

if n ==1:
    print(0)
    exit()

result = 0
def dfs(start):
    for newNode, cost in graph[start]:
        if visited[newNode]==-1:
            visited[newNode]= cost+visited[start]
            dfs(newNode)

visited[1]=0
dfs(1)
farwayNode = visited.index(max(visited))

visited=[-1 for _ in range(n+1)]
visited[farwayNode]=0

dfs(farwayNode)
print(max(visited))