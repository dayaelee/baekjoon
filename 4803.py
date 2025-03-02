import sys
input = sys.stdin.readline

def dfs(parent, node): # 1이 부모가 된다 (부모, 자식)
    visited[node]=True
    for child in graph[node]: 
        # print('child: ', child)
        if parent == child:# 양방향이면 노드의 부모도 걸릴 수 있음 
            continue # 루트   
        if visited[child]:
            return -1
        value = dfs(node, child) # 현재 노드, 현재 노드의 자식
        if value == -1:
            return -1
    # print('')
    return 1
     
graph=[]
numbering = 0
while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        exit()

    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b =map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(n+1)]
    result = 0
    for i in range(1, n+1):
        if visited[i] == False:
            value = dfs(0, i) # 1부터 시작 
            if value !=-1:
                result+=1

    numbering +=1

    if result>1:
        print("Case",str(numbering)+": A forest of", result,"trees.")
    elif result == 1:
        print("Case",str(numbering)+": There is one tree.")
    else:
        print("Case",str(numbering)+": No trees.")
