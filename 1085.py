x, y, w, h = map(int, input().split(" "))

num = []
for i in range(0, 4):
    num.append(0)

num[0] = h-y
num[1] = x-0
num[2] = w-x
num[3] = y-0

minimum = num[0]

for i in range(0, 4):
    if minimum >= num[i]:
        minimum = num[i]

print(minimum)
#x, y가 w, h에 포함된다고 생각하고 짬 그 외의 경우는 고려안했음 