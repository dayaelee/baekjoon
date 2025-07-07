import sys
n = int(input())
craneList = list(map(int, input().split()))
craneList.sort(reverse=True)
boxN = int(input())
boxs = list(map(int, input().split()))
boxs.sort(reverse=True)

time = 1
cnt = 0
totalCnt = 0
exit = 0
check2 = 0
visited = [False] * boxN
flag = 0
check2=0
while 1:
    check = 1
    cnt=totalCnt
    for i in range(n):
        check = 0
        for j in range(cnt, boxN):
            if boxs[j]<=craneList[i] and visited[j]==False:
                visited[j]=True
                check = 1
                cnt+=1
                check2+=1
                flag=0
                if check2==boxN:
                    print(time)
                    sys.exit(0)
                break
        
        if check ==0 and flag ==1:
            print(-1)
            sys.exit(0)
        
        if check ==0 and flag ==0:
            flag = 1
        
        if flag==1:
            break

    totalCnt+=1
    time+=1