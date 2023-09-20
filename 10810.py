n, m = map(int, input().split())

basket = []

for i in range(0, n):
     basket.insert(i, 0)

for i in range(0, m):
    i, j, k = map(int, input().split())
    for i in range(i, j+1):
         basket[i-1] = k
         
    #print(basket)


print(basket)