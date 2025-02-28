import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph=[[]for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

distance = [float("inf")] * (n+1)
distance[1] = 0
for i in range(n):
    for j in range(1, n+1):
        for k, cost in graph[j]:
            if distance[k]>distance[j]+cost:
                distance[k] = distance[j]+cost
                if i == n-1:
                    print(-1)
                    exit()

for i in range(2, n+1):
    if distance[i] == float("inf"):
        print(-1)
    else:
        print(distance[i])
