import sys
input=sys.stdin.readline
n, k = map(int, input().split())
dicM={}
for i in range(n):
    key = int(input().strip())
    dicM[key] = 0

dicM = sorted(dicM, reverse=True)

dicMM={}
for i in range(n):
    key = int(dicM[i])
    if int(key)<=k:
        if k//key>=1:
            dicMM[key]=k//key
            k=k%key
        else:
            dicMM[key] = 0
    else:
        dicMM[key] = 0

# print(dicMM)
# for key, value in dicM.items():
sum=0
for i, value in dicMM.items():
    sum+=value
print(sum)