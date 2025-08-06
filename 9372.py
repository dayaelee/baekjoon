import sys 
input = sys.stdin.readline

t = int(input())

def dfs(start):
    global cnt
    visited[start] = True

    for node in graph[start]:
        if visited[node]==False:
            cnt+=1
            dfs(node)

for i in range(t):
    n, m = map(int, input().split())
    graph = [[] for ii in range(n+1)]
    # print(graph)

    for j in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    visited=[False] * (n+1)
    # print(visited)
    global cnt
    
    cnt = 0
    for j in range(1, n+1):
        if visited[j] == False:
            dfs(j)
    print(cnt)