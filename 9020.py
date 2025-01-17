import sys
input = sys.stdin.readline

t = int(input())
def check(n):
    if n == 1:
        return False # 소수가 아니다
    for i in range(2, int(n**0.5) +1 ): # 소수 판별기 
        if n % i==0:
            return False # 소수가 아니다
    return True # 소수이다
        
for i in range(t):
    n = int(input())
    a = n//2
    b = n//2
    while 1:
        if a<0:
            break
        if a + b == n:
            if check(a) and check(b):
                print(a, b)
                break
            else:
                a-=1
                b+=1
