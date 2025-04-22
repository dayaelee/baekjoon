import sys
from collections import defaultdict
input = sys.stdin.readline


import heapq
n=int(input())
a=defaultdict(int)
for i in range(n):
    a[int(input())]+=1

for i in range(1, 10001):
    while a[i]>0:
        print(i)
        a[i]-=1

