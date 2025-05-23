# 번호표 선착순
import sys
n=int(input())
line = list(map(int, input().split()))
stack=[]
cnt=1
nstack=[]
for i in line:
    if i==cnt:
        nstack.append(i)
        cnt+=1
        while 1:
            if stack:
                if stack[-1]==cnt:
                    nstack.append(stack.pop())
                    cnt+=1
                else:
                    break
            else:
                break
    else:
        if stack:
            if stack[-1]==cnt:
                nstack.append(stack.pop())
                cnt+=1
            else:
                stack.append(i)
        else:
            stack.append(i)

total=nstack+stack[::-1]
for i in range(1, n+1):
    if i!=total[i-1]:
        print("Sad")
        sys.exit(0)
        break
print("Nice")