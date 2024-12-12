
from collections import deque

n = int(input())

tmp = [ i for i in range(1, n+1)]
tmp = deque(tmp)

while 1:
    if len(tmp)==1:
        print(tmp[0])
        break
    tmp.popleft()
    value = tmp.popleft()
    tmp.append(value)
