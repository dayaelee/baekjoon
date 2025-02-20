# 뮤탈리스크를 갖고있으면 무적?
# SCV는 각각 체력?

import sys
from collections import deque
input = sys.stdin.readline

heart=[]
n = int(input())
heart=list(map(int,input().split()))

df = [-9, -9, -3, -1, -3, -1]
ds = [-1, -3, -9, -9, -1, -3]
dt = [-3, -1, -1, -3, -9, -9]

dp = []
for i in heart:
    dp.append(i)
while len(dp)<3:
    dp.append(0)

global day
day = 0

def bfs(dp, day):
    q=deque([(dp[0], dp[1], dp[2], day)])
    heart.sort(reverse=True)
    
    while q:
        one, two, thr, day = q.popleft()
        #print(one, two, thr, day,'??')
        if one==two==thr==0:
            print(day)
            break

        for i in range(6):
            none = one + df[i]
            ntwo = two + ds[i]
            nthr = thr + dt[i]

            if none<=0:
                none = 0
            if ntwo <=0:
                ntwo = 0
            if nthr <= 0:
                nthr = 0

            #if dp[0] != none and dp[1] !=ntwo and dp[2] !=nthr:
            dp[0] = none
            dp[1] = ntwo
            dp[2] = nthr
            q.append((none, ntwo, nthr, day+1))

bfs(dp, day)