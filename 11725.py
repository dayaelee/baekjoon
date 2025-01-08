import sys
input = sys.stdin.readline

n = int(input())
dic={}
for i in range(n-1):
    a, b = map(int, input().split())
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [b]
    
    if b in dic:
        dic[b].append(a)
    else:
        dic[b] = [a]


#print(dic)

#  1
# 6  4 
# 3 2 7 
# 5

visited=[False for i in range(n+1)]



realDic = {}

def bfs(start):
    visited[start]=True
    queue=[start]
    while queue:
        value = queue.pop()
        for node in dic[value]:
            #print('node', node)
            #print(visited[node])
            if visited[node]== False:
                realDic[node]=value
                visited[node]=True
                queue.append(node)

bfs(1)

for i in range(2, n+1):
    print(realDic[i])

# print(realDic)