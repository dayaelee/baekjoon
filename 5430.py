import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

exception = [ '[', ']', ',']
for i in range(t):
    p = input().strip()

    p = deque(p)
    stack = []
    check = 0
    cnt = 0
    for PP in p:
        if PP=='R':
            check = 1
            cnt+=1
        else:
            if check == 1:
                check = 0
                if cnt%2!=0:
                    cnt = 0
                    stack.append('R')
            stack.append('D')
    if check ==1 and cnt==1:
        stack.append('R')
    elif cnt>1 and cnt %2!=0:
        stack.append('R')
        
    # print(p)
    # print(stack, 'stack')

    n = int(input())
    tmp = input()
    nList=deque([])
    nn=""
    for j in tmp:
        if j in exception:
            if len(nn)>0:
                nList.append(int(nn))
                nn=''
            continue
        else:
            nn+=j
    #print(nList)
    e1=0
    reverseFlag=0
    reverseFCnt = 0
    for q in stack:
        #print('stack', stack)
        if q == 'R':
            if reverseFlag ==1:
                reverseFlag = 0
            else:
                reverseFlag=1
            reverseFCnt+=1
        if q == 'D':
            if reverseFlag==0:
                if nList:
                    nList.popleft()
                else:
                    print('error')
                    e1=1
                    break
            else:
                # reverseFlag=0
                if nList:
                    nList.pop()
                else:
                    print('error')
                    e1=1
                    break
    
    #print('reverseFCnt', reverseFCnt)
    if e1!=1:
        strr="["
        if len(nList)>0:
            if reverseFCnt%2==0:
                for index, ii in enumerate(nList):
                    if index== len(nList)-1:
                        strr+=str(ii)+']'
                    else:
                        strr+=str(ii)+','
                print(strr, '!')
            else:
                nList.reverse()
                #print('??', nList)
                for index, ii in enumerate(nList):
                    if index== len(nList)-1:
                        strr+=str(ii)+']'
                    else:
                        strr+=str(ii)+','
                print(strr,'??')
        else:
            strr+="]"

            print(strr, '?')


# 3
# RDD
# 3
# [2, 1, 2]
# DDR
# 2
# [1, 2]
# D
# 3
# [1, 2, 3]