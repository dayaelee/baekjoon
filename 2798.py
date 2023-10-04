# n, m = map(int, input().split())

# llist=[]
# llist = list(map(int, input().split()))

# sumList=[]

# for i in range(0,n): 
#     for j in range(0,n): 
#         if i==j:
#             pass
#         else:
#             for k in range(0,n): 
#                 if i==j or j==k or k==i:
#                     pass
#                 else:
#                     # print("i j k",i, j, k)
#                     sumList.append(llist[i]+llist[j]+llist[k])

# smallM=m
# check=0
# while 1:
#     for i in range(0, len(sumList)):
#         if smallM==sumList[i]:
#             print(smallM)
#             check=1
#             break

#     if check==1:
#         break
#     else:
#         smallM=smallM-1
        
import sys

n,m = map(int, sys.stdin.readline().split())

bj = 0

lst = list(map(int, sys.stdin.readline().split()))

num = 0

sub=[]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            bj = bj + lst[i] + lst[j] + lst[k]
            diff = m - bj
            if diff >= 0 and m - num >= diff:
                num = bj
            bj = 0

print(num)
    

