import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().split())

# graph=defaultdict(list)
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    # graph[a]=[b, c]
    # graph[b]=[a, c]
    graph[a].append((b,c))
    graph[b].append((a,c))

visited=[False]*(n+1)
dis=[float('inf')]*(n+1)
visited[1]=True
dis[1]=0



tmp=[]
heapq.heappush(tmp, (0, 1))

while tmp:
    dist, now = heapq.heappop(tmp)

    if dis[now]<dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < dis[i[0]]:
            dis[i[0]] = cost
            heapq.heappush(tmp, (cost, i[0]))

ans =0
# print(dis)

# for i in dis:
#     if i == float('inf'):
#         continue
#     else:
#         ans=max(i, ans)
print(dis[n])