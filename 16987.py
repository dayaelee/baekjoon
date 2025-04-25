#
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
eggSet=[]
for i in range(n):
    eggSet.append(list(map(int, input().split())))

print('eggSet', eggSet)

def dfs(cnt, check):
    
    Anaegu, Aweight = eggSet[cnt][0], eggSet[cnt][1]

    nextCnt=cnt+1
    if eggSet:
        print('nextCnt, len(eggSet)', nextCnt, len(eggSet))
        if nextCnt<len(eggSet):
            while eggSet[nextCnt][0]>=0:
                nextCnt+=1
                print('nextCnt, len(eggSet)', nextCnt, len(eggSet))
                if nextCnt==len(eggSet):
                    print('?')
                    break
            Bnaegu, Bweight = eggSet[nextCnt][0], eggSet[nextCnt][1]

            eggSet[cnt][0]-=Bweight
            eggSet[nextCnt][0]-=Aweight

            if eggSet[cnt][0]<=0:
                check+=1
            if eggSet[nextCnt][0]<=0:
                check+=1



    print(eggSet)
    return eggSet

cnt=0
global check
check=0
while len(eggSet)>=2 and check<len(eggSet):
    if eggSet:
        if eggSet[cnt][0]>0:
            eggSet = dfs(cnt, check)
        else:
            cnt+=1
    else:
        break