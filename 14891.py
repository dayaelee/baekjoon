'''



총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 아래 그림과 같이 일렬로 놓여져

톱니는 N극 또는 S극 중 하나

톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 
그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번
-
이때, 톱니바퀴를 총 K번 회전

톱니바퀴의 회전은 한 칸을 기준

회전은 시계 방향과 반시계 방향이

-
톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 

톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 
회전시키지 않을 수도 있다. 


톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면,
B는 A가 회전한 방향과 반대방향

맞닿은 부분이 S극으로 서로 같기 때문에, 회전하지 않게 되
톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태
'''

import sys
from collections import deque
import copy
input = sys.stdin.readline
topni = []


for i in range(4):
    topni.append(input().strip())
k= int(input()) # 회전 횟수
howto=[]
#print(topni)
# 상태는 8개의 정수로 이루어져 있고,
# 12시방향부터 시계방향 순서대로 주어진다. 
# N극은 0, S극은 1로 나타나있다.
for i in range(k):
    num, dir = list(map(int,input().split())) # 회전톱니바퀴 번호, 방향 1= 시계, -1=반시계

# 항상 index[2]/ index[6], index[2]/index[6], index[2]/ index[6] 를 확인하면 됨

    pickTarget = num -1
    target=deque(topni[pickTarget])
    dirque = deque([(pickTarget, dir)])
    detailtarget=[[pickTarget, dir]]
    visited=[False for _ in range(4)]
    visited[pickTarget]=True
    #print('new')
    while dirque:
        check, dir = dirque.popleft()
        #print('check? dir', check, dir)
        
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
    
    #print('detailtarget', detailtarget)
    if detailtarget:
        for i in detailtarget:
            #print('i', i)
            pickTarget, dir = i
            #print('pickTarget, dir', pickTarget, dir)
            resultTarget=deque(topni[pickTarget])
            #print('resultTarget before', resultTarget)
            if dir == -1:
                tmp = resultTarget.popleft()
                resultTarget.append(tmp)
            else:
                tmp = resultTarget.pop()
                resultTarget.appendleft(tmp)
            #print('resultTarget after', ''.join(resultTarget))
            cvalue = ''.join(resultTarget)
            topni[pickTarget]=copy.deepcopy(cvalue)

    # for i in range(4):
    #     print('hi', topni[i])

result = 0
for i in range(4):
    #print('topni[i]', topni[i])
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

    
    



