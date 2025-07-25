import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(start):
    visited[start] = True
    path.append(start)
    next = s[start]

    if visited[next] == False:
        dfs(next)
    elif next in path:
        idx = path.index(next)
        # print('path[idx:] ', path[idx:])
        for i in path[idx:]:
            in_cycle[i]=True
        
    # print(path.pop())

for i in range(t):
    n = int(input())
    s = [0] + list(map(int, input().split()))

    visited=[False] * (n+1)
    in_cycle=[False] * (n+1)

    for j in range(1, n+1):
        if visited[j]==False:
            path=[]
            dfs(j)
    # print(sum(in_cycle))
    print(n-sum(in_cycle))
