import sys
from collections import deque
import copy
input = sys.stdin.readline
topni = []


for i in range(4):
    topni.append(input().strip())
k= int(input()) # 회전 횟수
howto=[]
for i in range(k):
    num, dir = list(map(int,input().split())) # 회전톱니바퀴 번호, 방향 1= 시계, -1=반시계

    pickTarget = num -1
    target=deque(topni[pickTarget])
    dirque = deque([(pickTarget, dir)])
    detailtarget=[[pickTarget, dir]]
    visited=[False for _ in range(4)]
    visited[pickTarget]=True
    while dirque:
        check, dir = dirque.popleft()
        if check == 0:
            if topni[check][2] == topni[check+1][6]:
                pass
            else:
                if visited[check+1]==False:
                    dirque.append([check+1, -dir])
                    
                    detailtarget.append([check+1, -dir])
                    visited[check]=True
            
        elif check == 1 or check ==2:
            if topni[check-1][2] == topni[check][6]:
                pass
            else:
                if visited[check-1]==False:
                    dirque.append([check-1, -dir])
                    
                    detailtarget.append([check-1, -dir])
                    visited[check]=True

            if topni[check][2] == topni[check+1][6]:
                pass
            else:
                if visited[check+1]==False:
                    dirque.append([check+1, -dir])
                    
                    detailtarget.append([check+1, -dir])
                    visited[check]=True

        elif check ==3:
            if topni[check-1][2] == topni[check][6]:
                pass
            else:
                if visited[check-1]==False:
                    dirque.append([check-1, -dir])
                    detailtarget.append([check-1, -dir])
                    visited[check]=True
    
    if detailtarget:
        for i in detailtarget:
            pickTarget, dir = i
            resultTarget=deque(topni[pickTarget])
            if dir == -1:
                tmp = resultTarget.popleft()
                resultTarget.append(tmp)
            else:
                tmp = resultTarget.pop()
                resultTarget.appendleft(tmp)
            cvalue = ''.join(resultTarget)
            topni[pickTarget]=copy.deepcopy(cvalue)

result = 0
for i in range(4):
    if i == 0:
        if topni[i][0]=='1':
            result+=1
    elif i == 1:
        if topni[i][0]=='1':
            result+=2
    elif i == 2:
        if topni[i][0]=='1':
            result+=4
    elif i == 3:
        if topni[i][0]=='1':
            result+=8

    
print(result)