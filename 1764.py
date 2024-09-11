import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dicN={}
dicM={}
result = []
check = 0
for i in range(n):
    key = input().strip()
    dicN[key] = 1

# print(dicN)

for j in range(m):
    key = input().strip()
    dicM[key] = 1

    if key in dicN:
        result.append(key)
        check = 1

if check == 1:
    print(len(result))
    result = sorted(result)
    for i in range(len(result)):
        print(result[i])
else:
    print(0)


