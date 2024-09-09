import sys
input = sys.stdin.readline
t = int(input())


def fibonacci(n, count):
    if n<=1:
        if n ==0:
            count[0]+=1
        if n==1:
            count[1]+=1

        print(count[0], count[1])
        return n
    
    a = 0
    b = 1

    for i in range(2, n+1):
        c = a + b
        a = b
        b = c


    print(a, b)
    return b 
        

for i in range(t):
    n = int(input())
    count = [0, 0]
    fibonacci(n, count)

# 0 1 1 2 3 5 8
