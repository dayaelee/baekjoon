doubleArr = [0 for _ in range(9)]
# 0을 9개 넣은 1차원 리스트로 초기화함

for i in range(9):
    doubleArr[i]= list(map(int, input().split(" ")))
    # 반복문을 돌면서, 각 인자에 리스트 추가 

max = 0
rememi = 0
rememj = 0
# 조회 
for i in range(9):
    for j in range(9):
        if max < doubleArr[i][j]:
            max = doubleArr[i][j]
            rememi = i+1
            rememj = j+1

if (rememi == 0 and rememj == 0):
    rememj = 1
    rememi = 1

print(max)
print(rememi, rememj)