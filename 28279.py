from collections import deque

n = int(input())
q=deque([])
for i in range(n):
    o=list(map(int, input().split()))

    if o[0]==1:
        q.appendleft(o[1])
    elif o[0]==2:
        q.append(o[1])
    elif o[0]==3:
        if q:
            print(q.popleft())
        else:
            print('-1')
    
    elif o[0]==4:
        if q:
            print(q.pop())
        else:
            print('-1')
    
    elif o[0]==5:
        print(len(q))

    elif o[0]==6:
        if q:
            print(0)
        else:
            print(1)
    
    elif o[0]==7:
        if q:
            print(q[0])
        else:
            print(-1)

    elif o[0]==8:
        if q:
            print(q[-1])
        else:
            print(-1)