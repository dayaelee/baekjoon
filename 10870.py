'''

0, 1


'''

n = int(input())
if n==0:
    print(0)
else:
    def fibonacci(n):
        a, b = 1, 1

        for _ in range(3, n+1):
            a, b = b, a+b
        
        return b

    print(fibonacci(n))
