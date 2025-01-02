tmp=[]
n = int(input())
tmp = list(map(int, input().split()))
dp=[]
for i in range(len(tmp)):
    if i == 0:
        dp.append(tmp[i])
    else:
        if dp[-1]+tmp[i]<=0:
            if tmp[i]>=0:
                dp.append(tmp[i])
            else:
                dp.append(0)
        else:
            dp.append(dp[-1]+tmp[i])

print(dp)

target = max(dp)
if target ==0:
    print(max(tmp))
else:
    print(target)