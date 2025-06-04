from collections import deque
import sys
input = sys.stdin.readline


def full(nodes):
    result = [-1]*(len(nodes)+1)
    for i in range(1, len(nodes)+1):
        if result[i]==-1:
            result[i]=0
            q = deque([i])

            # BFS를 돌며 인접 정점들에 반대 색을 전파
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if result[v] == -1:
                        # u가 0이면 v는 1, u가 1이면 v는 0
                        result[v] = 1 - result[u]
                        q.append(v)

    return result

def bfs(target):
    n = len(target)
    visited=[False] * (n+1)
    
    for i in range(1, n):
        if visited[i]==False:
            if target[i]==-1:
                print("NO")
                return 
            q=deque([(i)])
            visited[i]=True

            
            while q:
                node = q.popleft()
                # print(node,'???')
                for j in graph[node]:
                    if visited[j]==False:
                        if target[j]==-1:
                            print("NO")
                            return

                        if target[node]!= target[j]:
                            q.append(j)
                            visited[j]=True
                        else:
                            print("NO")
                            return
                    else:
                        if target[node]== target[j]:
                            print("NO")
                            return

    print('YES')
    return 


k= int(input())
for i in range(k):
    v, e = map(int, input().split())
    graph=[[] for _ in range(v+1)]
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    nodes=[i for i in range(1, v+1)]
    # print('graph', graph, 'v', v)
    result = full(nodes)
    # print('result', result)
    bfs(result)
    
    
    