n = int(input())
listt=[]
for i in range(n):
    listt.append(list(map(int, input().split())))


listt.sort(key = lambda x: (x[0], x[1]))

for i in listt:
    print(" ".join(map(str, i)))