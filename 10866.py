from collections import deque
import sys 
input = sys.stdin.readline

n = int(input())

result=[]
result = deque(result)

for i in range(n):
    tmp = input().split()
    if tmp[0] == 'push_back':
        result.append(tmp[1])
    elif tmp[0] == 'push_front':
        result.appendleft(tmp[1])
    elif tmp[0] == 'front':
        if result:
            print(result[0])
        else:
            print(-1)
    elif tmp[0] == 'back':
        if result:
            print(result[-1])
        else:
            print(-1)
    elif tmp[0] == 'size':
        if result:
            print(len(result))
        else:
            print(-1)
    elif tmp[0] == 'empty':
        if result:
            print(0)
        else:
            print(1)
    elif tmp[0] == 'pop_back':
        if result:
            print(result.pop())
        else:
            print(-1)
    elif tmp[0] == 'pop_front':
        if result:
            print(result.popleft())
        else:
            print(-1)
