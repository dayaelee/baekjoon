n, a, b = map(int, input().split())

if (a < b-n + n):
    print("Bus")
elif (a == b-n + n):
    print("Anything")
else:
    print("Subway")