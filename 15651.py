n, m = map(int, input().split())


def backtrack(tmp, cnt):
    for i in range(1, n+1):
        tmp.append(i)
        cnt+=1
        if cnt<m:
            backtrack(tmp, cnt)
        elif cnt==m:
            print(' '.join(map(str,tmp)))
        tmp.pop()
        cnt-=1


cnt=0
for i in range(1, n+1):
    tmp=[]
    tmp.append(i)
    cnt+=1
    if cnt<m:
        backtrack(tmp, cnt)
    elif cnt==m:
        print(' '.join(map(str,tmp)))
    cnt-=1
    tmp.pop()

