import sys
input=sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split()) # 부모, 자식
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(n+1)]
result = []

def dfs(x, cnt):
    global flag
    visited[x] = True
    if x == b:
        flag = True
        print(cnt)
    for val in graph[x]:
        if visited[val]==False:
            dfs(val, cnt+1)

flag = False
dfs(a, 0)
if flag==False:
    print(-1)
