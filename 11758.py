import sys
input = sys.stdin.readline

n=int(input())
k=int(input())
nList=list(map(int, input().split()))
nList.sort(reverse=True)
tmp=[]
for i in range(1, n):
    tmp.append(abs(nList[i]-nList[i-1]))
# print(nList)
tmp.sort(reverse=True)
# print(tmp)
tmp = tmp[k-1:]
print(sum(tmp))