n, m = map(int, input().split())
nL = list(map(int, input().split()))

answer=[]
def backtrack(ii, cnt, tmp):
    if cnt == m:
        print(' '.join(map(str, tmp)))
        answer.append(tmp[:])
        return 

    for i in range(ii, len(nL)):
        tmp.append(nL[i])
        backtrack(i, cnt+1, tmp)
        tmp.pop()
    return 

nL.sort()
cnt = 0
tmp=[]
backtrack(0, cnt, tmp)