import sys
input = sys.stdin.readline

n = int(input())
node = list(map(int, input().split()))
delete = int(input())


graph={}
start = -1
for i in range(len(node)):
    if node[i] == -1:
        start = i
        continue
    
    if node[i] not in graph:
        graph[node[i]]=[i]
    else:
        graph[node[i]].append(i)
# print(start)
# print(graph)


if delete == start:
    leaf=0
else:
    if delete in graph:
        del graph[delete] # 키 삭제 

    visited=[False for _ in range(n)]
    leaf = 0
    def dfs(start):
        global leaf 
        if start in graph:
            for node in graph[start]:
                if node == delete and len(graph[start])==1:
                    leaf+=1
                    visited[start]=True
                    continue

                if visited[node] == False:
                    visited[node] = True
                    dfs(node)
                    visited[node] = False
        else:
            if start != delete:
                leaf =leaf+1

    visited[start]=True
    dfs(start)

print(leaf)
