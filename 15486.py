
import sys
from collections import deque

input = sys.stdin.readline
tset=[]
pset=[]
n = int(input())
for i in range(n):
    t, p = map(int, input().split())
    tset.append(t)
    pset.append(p)

dp=[0]*(n+1)
print(dp)

waitT=deque([])
waitP=deque([])
for i in range(1, n+1):
    print('i waitT',i, waitT)
    print('i waitP',i, waitP)
    if waitT:
        waitT[0]


    if i < tset[i-1]:
        waitT.append(tset[i-1])
        waitP.append(pset[i-1])
    
    if tset[i-1]==1:
        if dp[i-1]<pset[i-1]:
            dp[i-1]+=pset[i-1]
print(dp)
