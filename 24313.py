a1, a0=map(int, input().split())
c=int(input())
n0=int(input())

if a1>c:
    answer=0
else:
    if ((a1-c)*n0) + a0<=0:
        answer=1
    else:
        answer=0

print(answer)
