n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))
nList.sort()

dic={}

for i in mList:
    if i not in dic:
        dic[i]=0

for i in nList:
    if i in dic:
        dic[i]+=1

answer = []
for i in mList:
    answer.append(dic[i])

print(' '.join(map(str, answer)))