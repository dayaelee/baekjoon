from collections import deque
n = int(input())
nlist=list(map(int, input().split()))
visited=[False] * (n+1)

poped=[1]
visited[1]=True

q=deque([i for i in range(1, n+1)])

now=0
rnow=1
while 1:
    if len(poped)==n:
        break
    value = nlist[now]

    if value>0:
        cnt=0
        while 1:
            rnow+=1
            if rnow>n:
                rnow=1
            if visited[rnow]==False:
                cnt+=1
            if cnt==value:
                visited[rnow]=True
                poped.append(rnow)
                break
            
    else:
        cnt=0
        while 1:
            rnow-=1
            if rnow<1:
                rnow=n
            if visited[rnow]==False:
                cnt+=1
            if cnt==abs(value):
                visited[rnow]=True
                poped.append(rnow)
                break
    now=rnow-1

print(' '.join(map(str, poped)))