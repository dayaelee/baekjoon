from collections import defaultdict

x = int(input()) # 참가자 수 
n = int(input()) # 참가 스태프 수 

tmp = []
dict = {}

limit = x*0.05

for i in range(n): # 스태프 정보 - 득표수 
    name, score = input().split()
    if int(score)>=limit:
        tmp.append([name, score])
        dict[name] = 0

tmpL = []
for i in range(1, 15):
    for j in range(len(tmp)):
        tmpL.append([tmp[j][0], str(int(tmp[j][1])//i)])

tmpL = sorted(tmpL, key = lambda x: -int(x[1]))

for i in range(14):
    key = tmpL[i][0]
    dict[key]+=1

for key, value in sorted(dict.items()):
    
    print(key, value)