n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
result =[]
def backtrack(cnt, result):
    #print(cnt, result)
    if cnt == m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(len(nlist)):
        result.append(nlist[i])
        backtrack(cnt+1, result)
        result.pop()

backtrack(0, result)


