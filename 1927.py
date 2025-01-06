import heapq

import sys
input = sys.stdin.readline

tmp = []
heapq.heapify(tmp)


n = int(input())
for i in range(n):
    check = int(input())
    if check != 0:
        heapq.heappush(tmp, check)
    else:
        if tmp:
            print(heapq.heappop(tmp))
        else:
            print(0)
