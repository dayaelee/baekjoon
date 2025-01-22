import sys
from collections import deque 
input = sys.stdin.readline

startS = input().strip()
m = int(input()) # 입력할 명령어의 개수
startS=list(startS)
rightS=deque([])

for i in range(m):
    tmp = input().split()
    if len(tmp)==1:
        if tmp[0]=='L':
            if len(startS)!=0:
                value = startS.pop()
                rightS.appendleft(value)
        elif tmp[0] == 'D':
            if len(rightS)!=0:
                value = rightS.popleft()
                startS.append(value)
        elif tmp[0] =='B':
            if len(startS)!=0:
                startS.pop()
    else:
        startS.append(tmp[1])
print(''.join(startS+list(rightS)))

