import math
n, s = map(int, input().split())

nlist = list(map(int, input().split()))
start, cnt = 0, 0
sum = nlist[0]
minlength = math.inf

while 1:
    if sum < s:
        cnt +=1
        if cnt == n:
            break
        sum += nlist[cnt]
    else:
        sum -= nlist[start]
        minlength = min(minlength, cnt - start +1)
        start+=1

if minlength == math.inf:
    print(0)
else:
    print(minlength)

