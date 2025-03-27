import heapq
import sys 
input = sys.stdin.readline

n, d = map(int, input().split())
roads=[]
mapp=[i for i in range(0, d+2)]

for i in range(n):
    roads.append(list(map(int, input().split())))

roads= sorted(roads)
# print(roads)

start = 0
mapp[0]=0
while 1:
    for i in roads:
        if i [1]<=d:
            if start == i[1]:
                # print('start', start)
                if i[0]==0:
                    if mapp[start]>i[2]:
                        mapp[start]=i[2]
                else:
                    if mapp[i[1]]>=mapp[i[0]]+i[2]:
                        # print('???')
                        mapp[i[1]] = mapp[i[0]]+i[2]
    start+=1
    #print(start,'???', mapp)
    if mapp[start]< mapp[start-1]+1:
        continue
    else:
        mapp[start]= mapp[start-1]+1

    if start == d+1:
        # for j in range(len(mapp)):
        #     print('j:', j, mapp[j])
        break
print(mapp[-2])
    