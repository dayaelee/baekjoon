n, m = map(int, input().split())
tmp = [i for i in range(1, n+1)]
result = []
def dfs():
    
    if len(result)==m:
        print(' '.join(map(str, result)))
        return 
    
    for i in range(n):
        if tmp[i] not in result:
            result.append(i+1)
            dfs()
            result.pop()

dfs()

