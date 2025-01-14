n, k = map(int, input().split())
visited=[False for i in range(200000+1)]
total =[]
def bfs(start, end):
    queue=[[start, 0]]
    visited[start]= True
    while queue:
        value, cnt = queue.pop(0)
        # print('value', value, 'cnt', cnt)
        if value == end:
            total.append(cnt)
            break
        
        if 0<=value +1<=200000:
            if visited[value+1]==False:
                visited[value + 1]=True
                queue.append([value + 1, cnt+1])
        if 0<=value *2<=200000:
            if visited[value*2]==False:
                visited[value * 2]=True
                queue.append([value * 2, cnt+1])
        if 0<=value - 1<=200000:
            if visited[value-1]==False:
                visited[value - 1]=True
                queue.append([value - 1, cnt+1])
        # print(queue)
    print(total[0])
        
        
bfs(n, k)
