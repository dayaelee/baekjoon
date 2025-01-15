from collections import deque

n, m = map(int, input().split())
queue = list(map(int, input().split()))

q = [i for i in range(1, n+1)]

leftq = deque(q)
rightq = deque(q)
reallcnt=0
realrcnt=0
total=0
for i in range(m):
    lcnt=0
    rcnt=0
    target = queue[i]
    leftq = deque(q)
    rightq = deque(q)
    while 1:
        if leftq[0] != target:
            lcnt+=1
            value = leftq.popleft()
            leftq.append(value)
        else:
            value = leftq.popleft()
            break
    
    target = queue[i]
    while 1:
        if rightq[0] != target:
            rcnt+=1
            value = rightq.pop()
            rightq.appendleft(value)
        else:
            value = rightq.popleft()
            break

    if lcnt<rcnt:
        q=leftq
    else:
        q=rightq
    
    total+=min(lcnt, rcnt)

print(total)