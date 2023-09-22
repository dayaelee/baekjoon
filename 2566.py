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

# list 추가로 만들기 
# 추가로 만든 list sort()하기 -> 맨 앞으로 가장 큰 값이 오도록
# 맨 앞줄 비교하기 + 가장 큰 값의 인덱스 저장

# 트리에 (최대값, (i , j))
max = 0
i = 0
j = 0

for _ in range(81):
    if max < input():
        max = input()

    i += 1
    j += 1
    if i % 10 == 0:
        i = 0
    
# 


if (rememi == 0 and rememj == 0):
    rememj = 1
    rememi = 1

print(max)
print(rememi, rememj)