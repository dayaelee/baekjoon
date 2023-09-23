stringList = []

# 초기화 
for i in range(0, 5):
    stringList.append(0)

maxlen = 0
for i in range(0, 5):
    stringList[i] = input()
    if maxlen < len(stringList[i]):
         maxlen = len(stringList[i])

#print(len(stringList[0]))

str = ""

for i in range(0, maxlen): #첫 줄의 글자수 
    for k in range(0, 5): # 다섯글자를 받으려고 함 
            if i >= len(stringList[k]):
                pass
            else:
                str = str + stringList[k][i]

#print(stringList)
print(str)