n, m = map(int, input().split())
all = sorted(list(map(int, input().split())))

visited=[False for i in range(n)]
#print(visited)


def backtrack(result, visited, cnt):
    #print(visited)
    if cnt == m:
        print(' '.join(map(str,result)))
        return 
    for i in range(n):
        if visited[i]==False:
            visited[i]=True
            result.append(all[i])
            backtrack(result, visited, cnt+1)
            result.pop()
            visited[i]=False

for i in range(n):
    cnt = 0
    result = []
    if visited[i]==False:
        visited[i]=True
        #print(visited,'????')
        result.append(all[i])
        backtrack(result, visited, cnt+1)
        result.pop()
        visited[i]=False
    


