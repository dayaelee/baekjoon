import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
alist=list(map(int, input().split()))
blist=list(map(int, input().split()))
m=int(input())
clist=list(map(int, input().split()))
result=[]
bag=deque([])
for i in range(n):
    if alist[i]==0:
        bag.append(blist[i])

for i in clist:
    bag.appendleft(i)
    result.append(bag.pop())
print(' '.join(map(str, result)))
