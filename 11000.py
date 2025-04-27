import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

n = int(input())
S = []

for i in range(n):
    s = list(map(int, input().split()))
    S.append(s)


S.sort()

hq = [] # 종료시간이 담김. h[0]은 가장 이른 종료시간대

for i in range(n):
    heapq.heappush(hq, S[i][1])
    if hq[0]<=S[i][0]: # 시작 시간이 종료 시간보다 뒤라면
        heapq.heappop(hq) # 한 강의실로 배정 

print(len(hq))


