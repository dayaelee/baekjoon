import sys
import heapq
input=sys.stdin.readline

n=int(input())
real=[]
heapq.heapify(real)
hi = []
heapq.heapify(hi)
for i in range(n):
    x=int(input())
    if x != 0:
        if x<0:
            heapq.heappush(hi, -x)
        else:
            heapq.heappush(real, x)
    else:
        if len(real)>0 and len(hi)>0:
            value1 = heapq.heappop(real)
            value2 = heapq.heappop(hi)
            if value1<value2:
                print(value1)
                heapq.heappush(hi, value2)
            elif value1 == value2:
                print(-value2)
                heapq.heappush(real, value1)
            elif value1>value2:
                print(-value2)
                heapq.heappush(real, value1)
        elif len(real)==0 and len(hi)>0:
            tmp = heapq.heappop(hi)
            print(-tmp)
        elif len(real)>0 and len(hi)==0:
            print(heapq.heappop(real))
        elif len(real)==0 and len(hi)==0:
            print(0)
# -4 3