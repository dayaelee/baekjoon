import sys
input = sys.stdin.readline

n = int(input())

mapp=[list(map(int, list(input().strip()))) for _ in range(n)]

def check(startY, startX, size):
    check0 = 0
    check1 = 0
    for i in range(startY, size):
        for j in range(startX, size):
            if mapp[i][j]==0:
                check0+=1
                
            else:
                check1+=1
    print('왜안나와?')            
    print(check0)
    print(check1)
    if check0==size*size:
        print(0)
    elif check1==size*size:
        print(1)
    if check0!=size*size and check1!=size*size:
        check(startY, startX, size//2)
        check(startY+size//2, startX, size//2)
        check(startY, startX+size//2, size//2)
        check(startY+size//2, startX+size//2, size//2)


check0 = 0
check1 = 0
for i in range(n):
    for j in range(n):
        if mapp[i][j]==0:
            check0+=1
        else:
            check1+=1
if check0==n*n:
    print('('+0)
elif check1==n*n:
    print('('+1)
else:
    check(0, 0, n//2)
    check(0, n//2, n//2)
    check(n//2, 0, n//2)
    check(n//2, n//2, n//2)

print(mapp)

