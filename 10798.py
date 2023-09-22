stringList = []

# 초기화 
for i in range(0, 5):
    stringList.append(0)

for i in range(0, 5):
    stringList[i] = input()

print(len(stringList[0]))

str = ""

for i in range(0, len(stringList[0])):
    for k in range(0, 5):
        for j in range(0, 5):
            if j >= len(stringList[k]):
                pass
            else:
                str = str + stringList[i][j]

print(stringList)