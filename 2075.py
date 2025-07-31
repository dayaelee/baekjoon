import sys 
input = sys.stdin.readline
import heapq

n = int(input())
mapp=[]
heapq.heapify(mapp)
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        
        heapq.heappush(mapp, tmp[j])
        if len(mapp)>n:
            heapq.heappop(mapp)

print(mapp[0])  

