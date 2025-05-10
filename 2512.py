
n = int(input())
mlist = sorted(list(map(int, input().split())))
result = int(input())
start=1
end=(mlist[n-1])
global flag
flag=0
while start<=end:
    mid = (start+end)//2
    # print(mid)
    sum=0
    flag=0
    for i in range(n):
        if mlist[i]<=mid:
            sum+=mlist[i]
        else:
            sum+=mid
    # print('sum', sum)
    if sum>result:
        end=mid-1
        flag+=1
    elif sum==result:
        print(mid)
        exit()
    else:
        start=mid+1

if flag==1:
    print(mid-1)
else:
    print(mid)
