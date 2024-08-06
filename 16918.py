# 크기 RxC 격자 
# 폭탄칸 3초 지난후 폭발 => 폭탄 칸 파괴되어 빈칸됨 => 인접한 네 칸도 파괴됨
# 만약 폭탄 폭발시 인접 네칸에 폭탄이 있는 경우, 해당 폭탄은 폭발없이 파괴됨 = 연쇄반응X

# 1. 일부 칸에 폭탄 설치 = 모든 폭탄이 설치된 시간은 같음 0초
# 2. 다음 1초 동안 아무것도 하지 않음
# 3. 다음 1초 동안 폭탄이 설치되지 않은 모든 칸에 폭탄 설치=모든 칸은 폭탄을 가짐 =동시에 설치
# 4. 1초 지난 후, 3초 전에 설치된 폭탄이 모두 폭발
# 5. 3-4 반복
import sys
input= sys.stdin.readline # 뒤에 괄호 붙이지 않도록 조심.

dy=[0, 0, 1, -1]
dx=[1, -1, 0, 0]

r, c, n = map(int, input().split()) 

bombMap = []
for i in range(r):
    tmp = list(input().strip())
    bombMap.append(tmp)

time = 0
for i in range(r):
    for j in range(c):
        if bombMap[i][j] == '.':
            bombMap[i][j]=0
        else:
            bombMap[i][j]=1

# 유지 time ==1
time+=1
for i in range(r):
    for j in range(c):
        if bombMap[i][j] > 0:
            bombMap[i][j]+=1

if n==1:
    if time == n:
        for i in range(r):
            tmpS=''
            for j in range(c):
                if bombMap[i][j]>0:
                    s='O'
                    tmpS+=s
                else:
                    s='.'
                    tmpS+=s
            print(tmpS)

else:
    while 1:
        time+=1
        
        if time % 4==1:
            # 유지
            for i in range(r):
                for j in range(c):
                    if bombMap[i][j] > 0:
                        bombMap[i][j]+=1
            rem = [item[:] for item in bombMap]  
            # 폭발
            for i in range(r):
                for j in range(c):
                    if rem[i][j]==3:
                        bombMap[i][j]=0
                        for k in range(4):
                            ni = i + dy[k]
                            nj = j + dx[k] 
                            if  0<=ni<r and 0<=nj<c: 
                                bombMap[ni][nj]=0
        elif time % 4 == 3:
            # 폭발
            rem = [item[:] for item in bombMap]  
            for i in range(r):
                for j in range(c):
                    if rem[i][j]==3:
                        bombMap[i][j]=0
                        for k in range(4):
                            ni = i + dy[k]
                            nj = j + dx[k] 
                            if  0<=ni<r and 0<=nj<c: 
                                bombMap[ni][nj]=0
        else:
            # 설치, 증가
            for i in range(r):
                    for j in range(c):
                        bombMap[i][j]+=1


        if time == n:
            for i in range(r):
                tmpS=''
                for j in range(c):
                    if bombMap[i][j]>0:
                        s='O'
                        tmpS+=s
                    else:
                        s='.'
                        tmpS+=s
                print(tmpS)
            break