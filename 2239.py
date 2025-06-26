import sys

b = []
for i in range(9):
    b.append(list(map(int, input())))

# print(b)
fill=[]
for i in range(0, 9):
    for j in range(0, 9):
        if b[i][j]==0:
            fill.append((i, j))

def backtrack(cnt):

    if len(fill)==cnt:
        for i in range(9):
            print(''.join(map(str, b[i])))
        sys.exit(0)

    y, x = fill[cnt] # 채워야 하는 위치 

    for i in range(1, 10): # 넣을 값
        out=0
        for j in range(9): # 같은 행 중에 값이 있는지?
            if b[y][j] == i:
                out = 1
                break
        if out ==1:
            continue
        
        out=0
        for j in range(9): # 같은 열 중에 값이 있는지? 
            if b[j][x] == i:
                out = 1
                break
        if out ==1:
            continue


        # (y//3)*3 # 시작점 
        # ((y//3)*3)+3 # 끝점
        out=0
        for jy in range((y//3)*3, ((y//3)*3)+3): # 9*9 중에 있는지? 
            for jx in range((x//3)*3, ((x//3)*3)+3):
                if b[jy][jx]==i:
                    out = 1
                    break
            if out ==1:
                continue
        if out ==1:
            continue
        
        b[y][x]=i
        backtrack(cnt+1)
        b[y][x]=0
    return 
    

backtrack(0)