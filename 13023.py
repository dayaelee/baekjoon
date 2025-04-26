import copy
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
global cycle
cycle=0

visited2=[False] *n
# print('graph', graph)

def dfs(start, cnt):
    # print('start, cnt', start, cnt)
    global cycle
    if cnt>=5:
        cycle+=1
        return

    for node in graph[start]:
        if visited[node]==False:
            visited[node]=True
            dfs(node, cnt+1)
            visited[node]=False

for i in range(n):
    visited=copy.deepcopy(visited2)
    # print('go! start, cnt', i, 1)
    visited[i]=True
    dfs(i, 1)
    visited[i]=False
    if cycle>=1:
        break

# print(cycle)
if cycle>=1:
    print(1)
else:
    print(0)