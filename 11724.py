import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tmp = []

dic={}

for i in range(1, n+1):
    dic[i]=[]
    
for i in range(m):
    u, v = map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)

#print(dic)

visited=[False for i in range(n)]
#print(visited)

def bfs(start):
    q=[start]
    while q:
        check = q.pop()
        for node in dic[check]:
            if visited[node-1] == False:
                visited[node-1] = True
                q.append(node)
cnt = 0
for key in dic.keys():
    if visited[key-1] == False:
        cnt+=1
        visited[key-1] = True
        bfs(key)
    
print(cnt)
