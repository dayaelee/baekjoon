'''

단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료

'''

from collections import deque 

n, m, v = map(int, input().split())

dic={}
node = [i for i in range(1, n+1)]

visited=[[False] for _ in range(n)]
# print(visited)

for i in range(m):
    a, b = map(int, input().split())
    if a in dic:
        dic[a].append(b)
    else:
        dic[a]=[b]

    if b in dic:
        dic[b].append(a)
    else:
        dic[b]=[a]


# dictionary의 모든 요소 정렬

# 딕셔너리 키는 자동 정렬되는가? 
# print(dic)
for key, value in dic.items():
    dic[key] = sorted(value)
# print(dic)


resultBFS=[]
resultDFS=[]

def bfs(start):
    queue=deque([start])

    while queue:
        node = queue.popleft()
        if node in dic:
            for i in dic[node]:
                if visited[i-1] == True:
                    continue
                else:
                    visited[i-1]=True
                    resultBFS.append(i)
                    queue.append(i)

def dfs(start):
    if start in dic:
        for i in dic[start]:
                if visited[i-1] == True:
                    continue
                else:
                    visited[i-1]=True
                    resultDFS.append(i)
                    dfs(i)

resultDFS=[node[v-1]]
visited[v-1]=True
dfs(node[v-1])
visited=[[False] for _ in range(n)]

resultBFS=[node[v-1]]
visited[v-1]=True
bfs(node[v-1])


print(' '.join(list(map(str, resultDFS))))
print(' '.join(list(map(str, resultBFS))))
