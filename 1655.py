import sys
import heapq
input = sys.stdin.readline

n = int(input())

low = []
high = []

for i in range(n):
    x = int(input())
    if not low or x<=-low[0]:
        heapq.heappush(low, -x)
    else:
        heapq.heappush(high, x)
    # print( 'low ', low)
    # print( 'high ', high)

    if len(low) < len(high):
        heapq.heappush(low, -heapq.heappop(high))
    elif len(low) > len(high) + 1:
        heapq.heappush(high, -heapq.heappop(low))

    
    if high and -low[0] > high[0]:
        heapq.heappush(high, -heapq.heappop(low))
        heapq.heappush(low, -heapq.heappop(high))

    # print( 'low ', low)
    # print( 'high ', high)
    print(-low[0])

    
        


    