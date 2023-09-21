n, m = map(int, input().split())

basket = []
a = []

for i in range(0, n):
    basket.append(i+1)

for i in range(0, m):
    ii, j = map(int, input().split())
    a = basket[ii-1:j]
    a.reverse()
    b = 0
    for k in range(ii, j+1):
        basket[k-1] = a[b]
        b = b + 1
    
print(*basket)