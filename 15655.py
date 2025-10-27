n, m = map(int, input().split())

a = list(map(int, input().split()))

tmp = []

a = sorted(a)

visited = [False for _ in range(len(a))]


tmp =[]
cnt = 0
def backtrack(now, cnt, tmp):
    if cnt==m:
        print(' '.join(map(str, tmp)))
        return 

    for i in range(now, len(a)):
        if visited[i]==False:
            tmp.append(a[i])
            visited[i]=True
            backtrack(i, cnt+1, tmp)
            tmp.pop()
            visited[i]=False

backtrack(0, cnt, tmp)

            

