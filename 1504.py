import sys
import heapq
import math
input = sys.stdin.readline

n, e = map(int, input().split())
graph=[[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

def dijkstra(start):
    dist = [float("inf") for _ in range(n+1)]
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        distance, node = heapq.heappop(q)
        if dist[node]<distance:
            continue
        
        for newNode, cost  in graph[node]:
            newCost = dist[node]+cost
            if dist[newNode]>newCost:
                dist[newNode] = newCost
                heapq.heappush(q, (newCost, newNode))
    return dist

origin_dist = dijkstra(1)
v1_dist = dijkstra(v1) # v1에서 나아가는거 
v2_dist = dijkstra(v2)

if origin_dist[v1] == math.inf or  v1_dist[v2] ==math.inf or v2_dist[n] == math.inf or v2_dist[v1]==math.inf:
    print(-1)
else:
    v1_path = origin_dist[v1] + v1_dist[v2] + v2_dist[n]
    v2_path = origin_dist[v2] + v2_dist[v1] + v1_dist[n]
    print((min(v1_path, v2_path)))



