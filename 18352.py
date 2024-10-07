'''
최단 거리가 정확히 K인 모든 도시들의 번호를 
출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1

 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 
 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성

'''
import heapq
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

mapp =[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    mapp[a].append([b, 1])

costs=[1e9 for _ in range(n+1)]
costs[1]=0
heap=[]
heapq.heappush(heap, [0, x])

while heap:
    cur_cost, cur_node = heapq.heappop(heap)
    if costs[cur_node] < cur_cost: # 현재 노드의 비용보다 기록된 노드의 비용이 더 작을 경우 패스
        continue
    for next_node, next_cost in mapp[cur_node]:
        if cur_cost+next_cost > costs[next_node]: 
            # 현재+다음 노드비용이 기록된 다음 노드 비용보다 크면 패스
            continue

        costs[next_node] = cur_cost+next_cost
        heapq.heappush(heap, [costs[next_node], next_node])

#print(costs)
check = 0
for index, i in enumerate(costs):
    if i == k:
        check = 1
        print(index)
if check==0:
    print(-1)

