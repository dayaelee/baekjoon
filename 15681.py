import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, r, q = map(int, input().split())
graph={}
for i in range(n-1):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

visited = [False for _ in range(n+1)]

dp=[0 for _ in range(n+1)]

def DFS(node):
    dp[node]=1
    for newNode in graph[node]:
        if not dp[newNode]:
            DFS(newNode)
            dp[node]+= dp[newNode]
DFS(r)

for i in range(q):
    u = int(input())
    print(dp[u])