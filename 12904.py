from collections import deque
import sys
s = input()
t = input()

q=deque([(list(t))])
check = 0

while q:
    # print(q)
    value =q.popleft()
    # print('len(value) == len(s)', len(value) == len(s))
    if len(value) == len(s):
        # print('s==value', s, ''.join(value))
        if s==''.join(value):
            print(1)
            check = 1
            break
    elif len(value) >0:
        if value[-1]=='A':
            q.append(value[:-1])
        if value[-1] == 'B':
            valuetwo=value[:-1]
            q.append(valuetwo[::-1])
        
if check == 0:
    print(0)