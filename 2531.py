import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
dishes=[]
q = []
for i in range(n):
    tmp = int(input())
    dishes.append(tmp)
    if i <k:
        q.append(tmp)
# print('q', q)
end = k-1
answer=0
check = 0
while 1:
    
    qs = set(q)
    
    if c not in qs:
        result = len(qs)+1
    else:
        result = len(qs)
    
    answer = max(answer, result)
    q = deque(q)
    q.popleft()
    end+=1

    

    if end == n:
        end = 0
        check =1
        
    
    q.append(dishes[end])

    if check ==1 and end == k:
        break
print(answer)