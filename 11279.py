'''
# 최대 힙
'''
import heapq
import sys
input = sys.stdin.readline
n = int(input())

tmp = []
for i in range(n):
    value = int(input())
    if value !=0:
        heapq.heappush(tmp, -value)
    else:
        if not tmp:
            print(0)
        else:
            print(-heapq.heappop(tmp))