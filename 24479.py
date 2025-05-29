import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph=[[] for i in range(n+1)]
visited=[False] * (n+1)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited[r]=True

dic={}
global cnt
cnt = 1

def dfs(n, cnt, f):
    visited[n]=True
    if f==1:
        dic[n]=cnt
        check=0
        if graph[n]:
            for node in sorted(graph[n]):
                if visited[node]== False:
                    check=1
                    cnt = dfs(node, cnt+1, 1)
            if check==0:
                if not dic[node]:
                    dic[node]=0
    else:
        check=0
        if graph[n]:
            for node in sorted(graph[n]):
                if visited[node]== False:
                    check=1
                    dfs(node, cnt+1, 0)
            if check==0:
                dic[n]=0
    return cnt
    
dfs(r, 1, 1)

for i in range(1, n+1):
    if visited[i]==False:
        dfs(i, 1, 0)
    
for i in range(1, n+1):
    if i not in dic:
        print(0)
    else:
        print(dic[i])