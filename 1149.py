import sys
input = sys.stdin.readline
n = int(input())


mapp=[]
for i in range(n):
    mapp.append(list(map(int, input().split())))
dp=[]
for j in range(n):
    if j == 0:
        dp.append(mapp[0])
    else:
        tmp=[]
        for i in range(3):
            if i ==0:
                tmp.append(min(dp[-1][1]+mapp[j][0], dp[-1][2]+mapp[j][0]))
            elif i == 1:
                tmp.append(min(dp[-1][0]+mapp[j][1], dp[-1][2]+mapp[j][1]))
            elif i ==2:
                tmp.append(min(dp[-1][0]+mapp[j][2], dp[-1][1]+mapp[j][2]))
        dp.append(tmp)
print(min(dp[-1]))
    

