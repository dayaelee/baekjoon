n = int(input())

def recursion(n, start, end):
    if n == 1:
        print(start, end)
        return

    recursion(n-1, start, 6-start-end)
    print(start, end)
    recursion(n-1, 6-start-end, end)


print(2**n-1)
recursion(n, 1, 3)
