big = 0
tmp2=[0, 0]
for i in range(5):
    tmp = list(map(int, input().split()))
    sum = 0
    for j in tmp:
        sum+=j

    if big < sum:

        tmp2[0] = i+1
        tmp2[1] = sum
        big = sum

print(tmp2[0], tmp2[1])
    