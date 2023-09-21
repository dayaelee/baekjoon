n, m = map(int, input().split())

basket = []

for i in range(1, n+1):
    basket.insert(i, i)

for i in range(0, m):
    i, j = map(int, input().split())
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp


print(*basket)