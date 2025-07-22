
import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
listA=[]
graph=[[] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    global idx
    for j in range(len(tmp)):
        if j ==0:
            idx = tmp[j]
        else:
            if j%2!=0:
                if tmp[j]==-1:
                    break
                else:
                    graph[idx-1].append((tmp[j], tmp[j+1]))
            else:
                continue

def bfs(start):
    visited=[False] * n
    global answer
    answer = 0
    q=deque([(start, 0)])
    visited[start]=True
    global remNode
    remNode = -1
    while q:
        node, nowDis = q.popleft()
        for nnode, dist in graph[node]:
        
            if visited[nnode-1]==False:
                visited[nnode-1]=True
                newDis=nowDis+dist
                if answer < newDis:
                    remNode=nnode-1
                    answer=newDis 
                q.append((nnode-1, newDis))
    return remNode


u = bfs(1)
bfs(u)

print(answer)
    

