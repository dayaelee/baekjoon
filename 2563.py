# 1. 색종이 수 만큼 넓이를 구한후
# 2. 색종이 끼리 겹치는 곳에서의 넓이를 뺀다 

n = int(input())

doubleArr = []
totall = list()

for i in range(0, n):
    doubleArr.append(0) # 1차원 배열 생성

for i in range(0, 100):
    tmp = []
    for j in range(0, 100):
       tmp.append(0)
    totall.append(tmp)
    
# print("")
# print("total", len(totall))

for i in range(0, n):
    # i는 가로 j는 세로
    doubleArr[i] = list(map(int, input().split(" ")))

for i in range(0, n):
    x = doubleArr[i][0]
    y = doubleArr[i][1]
    for a in range(0, 10):
        for b in range(0, 10):
            #print("x: ", x, "y: ", y)
            totall[x][y] = 1
            y = y + 1
        x = x + 1
        y = y - 10
    x = x - 10

total = 10 * 10 * n
sub = 0

for a in range(0, 100):
    for b in range(0, 100):
        if (totall[a][b]==1):
            sub = sub + 1

print(sub)
#print("total")
#print(totall)
