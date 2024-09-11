n = int(input())
tmp = list(map(int, input().split()))

tmp = sorted(tmp)
sum = 0
for i in range(n):
    if i == 0:
        sum+=tmp[i]
        continue

    tmp[i]=tmp[i-1]+tmp[i]
    sum+=tmp[i]

# 1 2 3 3 4
print(sum)

